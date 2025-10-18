"""
Upgrade UI System - Visual interface for character development
"""

import pygame
import math
import random
from src.settings import *

class UpgradeUI:
    """Visual upgrade screen with skill tree"""
    
    def __init__(self):
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
        # UI state
        self.selected_skill = None
        self.hover_skill = None
        
        # Colors
        self.bg_color = (20, 20, 40)
        self.panel_color = (40, 40, 80)
        self.accent_color = (100, 200, 255)
        self.upgrade_color = (50, 200, 100)
        self.locked_color = (100, 100, 100)
        
    def draw_upgrade_screen(self, screen, character_stats):
        """Draw the complete upgrade interface"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(self.bg_color)
        screen.blit(overlay, (0, 0))
        
        # Draw panels
        self.draw_character_panel(screen, character_stats)
        self.draw_skill_tree(screen, character_stats)
        self.draw_stats_panel(screen, character_stats)
        self.draw_abilities_panel(screen, character_stats)
        
        # Instructions
        instructions = "Click skill to upgrade | ESC to close"
        text = self.font_small.render(instructions, True, WHITE)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT - 30))
    
    def draw_character_panel(self, screen, stats):
        """Draw character info panel"""
        panel_rect = pygame.Rect(20, 20, 300, 150)
        pygame.draw.rect(screen, self.panel_color, panel_rect, border_radius=10)
        pygame.draw.rect(screen, self.accent_color, panel_rect, 2, border_radius=10)
        
        y_offset = 35
        
        # Level
        level_text = self.font_large.render(f"LEVEL {stats.level}", True, self.accent_color)
        screen.blit(level_text, (panel_rect.x + 20, panel_rect.y + 15))
        
        # XP Bar
        xp_bar_rect = pygame.Rect(panel_rect.x + 20, panel_rect.y + 70, 260, 25)
        pygame.draw.rect(screen, (60, 60, 100), xp_bar_rect, border_radius=5)
        
        xp_ratio = stats.xp / stats.xp_to_next_level
        fill_width = int(xp_bar_rect.width * xp_ratio)
        if fill_width > 0:
            fill_rect = pygame.Rect(xp_bar_rect.x, xp_bar_rect.y, fill_width, xp_bar_rect.height)
            pygame.draw.rect(screen, self.upgrade_color, fill_rect, border_radius=5)
        
        pygame.draw.rect(screen, self.accent_color, xp_bar_rect, 2, border_radius=5)
        
        # XP Text
        xp_text = self.font_small.render(f"{stats.xp} / {stats.xp_to_next_level} XP", True, WHITE)
        screen.blit(xp_text, (xp_bar_rect.centerx - xp_text.get_width()//2, 
                             xp_bar_rect.centery - xp_text.get_height()//2))
        
        # Skill Points
        sp_text = self.font_medium.render(f"Skill Points: {stats.skill_points}", True, YELLOW)
        screen.blit(sp_text, (panel_rect.x + 20, panel_rect.y + 110))
    
    def draw_skill_tree(self, screen, stats):
        """Draw skill tree with upgrade buttons"""
        panel_rect = pygame.Rect(20, 190, 600, 350)
        pygame.draw.rect(screen, self.panel_color, panel_rect, border_radius=10)
        pygame.draw.rect(screen, self.accent_color, panel_rect, 2, border_radius=10)
        
        # Title
        title = self.font_large.render("SKILL TREE", True, self.accent_color)
        screen.blit(title, (panel_rect.x + 20, panel_rect.y + 15))
        
        # Skills layout (grid)
        skills_info = [
            {"name": "speed", "icon": "⚡", "desc": "Movement Speed"},
            {"name": "jump", "icon": "🦘", "desc": "Jump Power"},
            {"name": "boost", "icon": "🚀", "desc": "Boost Duration"},
            {"name": "energy", "icon": "⚙️", "desc": "Max Energy"},
            {"name": "shield", "icon": "🛡️", "desc": "Shield Duration"},
            {"name": "magnet", "icon": "🧲", "desc": "Coin Magnet"},
        ]
        
        cols = 3
        skill_size = 140
        spacing = 20
        start_x = panel_rect.x + 40
        start_y = panel_rect.y + 80
        
        mouse_pos = pygame.mouse.get_pos()
        
        for i, skill_info in enumerate(skills_info):
            row = i // cols
            col = i % cols
            
            x = start_x + col * (skill_size + spacing)
            y = start_y + row * (skill_size + spacing)
            
            skill_rect = pygame.Rect(x, y, skill_size, skill_size)
            skill_name = skill_info["name"]
            skill_data = stats.skills[skill_name]
            
            # Check if hovering
            is_hover = skill_rect.collidepoint(mouse_pos)
            if is_hover:
                self.hover_skill = skill_name
            
            # Determine color
            if skill_data["level"] >= skill_data["max"]:
                color = (100, 200, 100)  # Maxed out
            elif stats.skill_points >= skill_data["cost"]:
                color = self.upgrade_color if not is_hover else (70, 230, 120)
            else:
                color = self.locked_color
            
            # Draw skill box
            pygame.draw.rect(screen, color, skill_rect, border_radius=8)
            if is_hover:
                pygame.draw.rect(screen, WHITE, skill_rect, 3, border_radius=8)
            else:
                pygame.draw.rect(screen, self.accent_color, skill_rect, 2, border_radius=8)
            
            # Icon
            icon_text = self.font_large.render(skill_info["icon"], True, WHITE)
            screen.blit(icon_text, (x + skill_size//2 - icon_text.get_width()//2, y + 10))
            
            # Name
            name_text = self.font_small.render(skill_info["desc"], True, WHITE)
            screen.blit(name_text, (x + skill_size//2 - name_text.get_width()//2, y + 60))
            
            # Level
            level_text = self.font_medium.render(
                f"{skill_data['level']}/{skill_data['max']}", True, WHITE
            )
            screen.blit(level_text, (x + skill_size//2 - level_text.get_width()//2, y + 85))
            
            # Cost
            cost_text = self.font_small.render(f"Cost: {skill_data['cost']}", True, YELLOW)
            screen.blit(cost_text, (x + skill_size//2 - cost_text.get_width()//2, y + 115))
            
            # Store rect for click detection
            skill_data["ui_rect"] = skill_rect
    
    def draw_stats_panel(self, screen, stats):
        """Draw character statistics"""
        panel_rect = pygame.Rect(640, 190, 280, 220)
        pygame.draw.rect(screen, self.panel_color, panel_rect, border_radius=10)
        pygame.draw.rect(screen, self.accent_color, panel_rect, 2, border_radius=10)
        
        # Title
        title = self.font_medium.render("STATS", True, self.accent_color)
        screen.blit(title, (panel_rect.x + 20, panel_rect.y + 15))
        
        # Stats list
        stat_list = [
            f"Speed: {stats.speed:.1f}",
            f"Jump: {stats.jump_power:.0f}",
            f"Boost: {stats.boost_power:.2f}x",
            f"Max Energy: {stats.max_energy}",
            f"Energy Regen: {stats.energy_regen}/s",
        ]
        
        y_offset = 55
        for i, stat_text in enumerate(stat_list):
            text = self.font_small.render(stat_text, True, WHITE)
            screen.blit(text, (panel_rect.x + 20, panel_rect.y + y_offset + i * 30))
    
    def draw_abilities_panel(self, screen, stats):
        """Draw unlocked abilities"""
        panel_rect = pygame.Rect(640, 430, 280, 110)
        pygame.draw.rect(screen, self.panel_color, panel_rect, border_radius=10)
        pygame.draw.rect(screen, self.accent_color, panel_rect, 2, border_radius=10)
        
        # Title
        title = self.font_medium.render("ABILITIES", True, self.accent_color)
        screen.blit(title, (panel_rect.x + 20, panel_rect.y + 15))
        
        # Abilities
        abilities_info = [
            ("double_jump", "Double Jump"),
            ("dash", "Dash"),
            ("shield_regen", "Shield Regen"),
            ("coin_magnet", "Coin Magnet"),
        ]
        
        y_offset = 55
        for i, (ability_key, ability_name) in enumerate(abilities_info):
            unlocked = stats.abilities[ability_key]
            color = self.upgrade_color if unlocked else self.locked_color
            status = "✓" if unlocked else "✗"
            
            text = self.font_small.render(f"{status} {ability_name}", True, color)
            screen.blit(text, (panel_rect.x + 20, panel_rect.y + y_offset + i * 25))
    
    def draw_energy_bar(self, screen, stats, x, y, width=200, height=20):
        """Draw energy bar for HUD"""
        # Background
        bg_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (40, 40, 40), bg_rect, border_radius=5)
        
        # Fill
        fill_ratio = stats.energy / stats.max_energy
        fill_width = int(width * fill_ratio)
        if fill_width > 0:
            fill_rect = pygame.Rect(x, y, fill_width, height)
            # Gradient effect
            color = (50, 200, 255) if fill_ratio > 0.3 else (255, 100, 100)
            pygame.draw.rect(screen, color, fill_rect, border_radius=5)
        
        # Border
        pygame.draw.rect(screen, (100, 200, 255), bg_rect, 2, border_radius=5)
        
        # Text
        text = self.font_small.render(f"Energy: {int(stats.energy)}/{stats.max_energy}", True, WHITE)
        screen.blit(text, (x + width//2 - text.get_width()//2, y - 25))
    
    def handle_click(self, pos, stats):
        """Handle mouse click on upgrade screen"""
        for skill_name, skill_data in stats.skills.items():
            if "ui_rect" in skill_data and skill_data["ui_rect"].collidepoint(pos):
                if stats.upgrade_skill(skill_name):
                    return True  # Upgrade successful
                return False  # Upgrade failed
        return None  # No skill clicked


class ParticleSystem:
    """Advanced particle effects"""
    
    def __init__(self):
        self.particles = []
    
    def emit(self, x, y, count=10, particle_type="default"):
        """Emit particles"""
        for _ in range(count):
            if particle_type == "level_up":
                particle = {
                    "x": x,
                    "y": y,
                    "vx": random.uniform(-100, 100),
                    "vy": random.uniform(-200, -100),
                    "life": random.uniform(1.0, 2.0),
                    "max_life": 2.0,
                    "size": random.randint(3, 8),
                    "color": random.choice([(255, 215, 0), (255, 255, 100), (255, 200, 50)])
                }
            elif particle_type == "boost":
                particle = {
                    "x": x,
                    "y": y,
                    "vx": random.uniform(-150, -50),
                    "vy": random.uniform(-30, 30),
                    "life": random.uniform(0.3, 0.6),
                    "max_life": 0.6,
                    "size": random.randint(2, 5),
                    "color": (255, 150, 50)
                }
            else:  # default
                particle = {
                    "x": x,
                    "y": y,
                    "vx": random.uniform(-50, 50),
                    "vy": random.uniform(-100, -50),
                    "life": random.uniform(0.5, 1.0),
                    "max_life": 1.0,
                    "size": random.randint(2, 4),
                    "color": (200, 200, 200)
                }
            
            self.particles.append(particle)
    
    def update(self, dt):
        """Update all particles"""
        for particle in self.particles[:]:
            particle["x"] += particle["vx"] * dt
            particle["y"] += particle["vy"] * dt
            particle["vy"] += 300 * dt  # Gravity
            particle["life"] -= dt
            
            if particle["life"] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        """Draw all particles"""
        for particle in self.particles:
            alpha_ratio = particle["life"] / particle["max_life"]
            size = int(particle["size"] * alpha_ratio)
            if size > 0:
                pygame.draw.circle(screen, particle["color"],
                                 (int(particle["x"]), int(particle["y"])), size)
