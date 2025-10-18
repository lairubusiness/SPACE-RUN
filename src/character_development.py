"""
Advanced Character Development System
RPG-style progression with attributes, skills, and upgrades
"""

import pygame
import json
import math
import random
from src.settings import *

class CharacterStats:
    """Manages character attributes and progression"""
    
    def __init__(self):
        # Core attributes
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
        
        # Movement attributes
        self.speed = 8.0
        self.jump_power = 600.0
        self.boost_power = 1.5
        self.air_control = 0.7
        
        # Energy system
        self.max_energy = 100
        self.energy = 100
        self.energy_regen = 5  # per second
        
        # Upgrade points
        self.skill_points = 0
        
        # Skill tree
        self.skills = {
            "speed": {"level": 0, "max": 10, "cost": 1},
            "jump": {"level": 0, "max": 10, "cost": 1},
            "boost": {"level": 0, "max": 10, "cost": 1},
            "energy": {"level": 0, "max": 10, "cost": 1},
            "shield": {"level": 0, "max": 5, "cost": 2},
            "magnet": {"level": 0, "max": 5, "cost": 2},
        }
        
        # Passive abilities unlocked
        self.abilities = {
            "double_jump": False,
            "dash": False,
            "shield_regen": False,
            "coin_magnet": False,
        }
        
        # Statistics
        self.total_distance = 0
        self.total_jumps = 0
        self.total_boosts = 0
        self.enemies_dodged = 0
        self.coins_collected = 0
    
    def gain_xp(self, amount):
        """Add XP and handle level ups"""
        self.xp += amount
        levels_gained = 0
        
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            levels_gained += 1
            self.skill_points += 2  # 2 points per level
            self.xp_to_next_level = int(100 * (1.2 ** (self.level - 1)))
            
            # Level up bonuses
            self.max_energy += 10
            self.energy = self.max_energy
        
        return levels_gained
    
    def upgrade_skill(self, skill_name):
        """Upgrade a skill if possible"""
        if skill_name not in self.skills:
            return False
        
        skill = self.skills[skill_name]
        
        if skill["level"] >= skill["max"]:
            return False  # Max level
        
        if self.skill_points < skill["cost"]:
            return False  # Not enough points
        
        # Perform upgrade
        self.skill_points -= skill["cost"]
        skill["level"] += 1
        
        # Apply upgrade effects
        self.apply_skill_effects(skill_name)
        
        # Check for ability unlocks
        self.check_ability_unlocks()
        
        return True
    
    def apply_skill_effects(self, skill_name):
        """Apply the effects of a skill upgrade"""
        if skill_name == "speed":
            self.speed = 8.0 + (self.skills["speed"]["level"] * 1.5)
        elif skill_name == "jump":
            self.jump_power = 600.0 + (self.skills["jump"]["level"] * 50)
        elif skill_name == "boost":
            self.boost_power = 1.5 + (self.skills["boost"]["level"] * 0.15)
        elif skill_name == "energy":
            self.max_energy = 100 + (self.skills["energy"]["level"] * 20)
            self.energy_regen = 5 + (self.skills["energy"]["level"] * 1)
    
    def check_ability_unlocks(self):
        """Check if any abilities should be unlocked"""
        if self.skills["jump"]["level"] >= 5 and not self.abilities["double_jump"]:
            self.abilities["double_jump"] = True
        
        if self.skills["boost"]["level"] >= 5 and not self.abilities["dash"]:
            self.abilities["dash"] = True
        
        if self.skills["shield"]["level"] >= 3 and not self.abilities["shield_regen"]:
            self.abilities["shield_regen"] = True
        
        if self.skills["magnet"]["level"] >= 2 and not self.abilities["coin_magnet"]:
            self.abilities["coin_magnet"] = True
    
    def use_energy(self, amount):
        """Use energy if available"""
        if self.energy >= amount:
            self.energy -= amount
            return True
        return False
    
    def regen_energy(self, dt):
        """Regenerate energy over time"""
        self.energy = min(self.max_energy, self.energy + self.energy_regen * dt)
    
    def get_save_data(self):
        """Get data for saving"""
        return {
            "level": self.level,
            "xp": self.xp,
            "skill_points": self.skill_points,
            "skills": self.skills,
            "abilities": self.abilities,
            "stats": {
                "total_distance": self.total_distance,
                "total_jumps": self.total_jumps,
                "total_boosts": self.total_boosts,
                "enemies_dodged": self.enemies_dodged,
                "coins_collected": self.coins_collected,
            }
        }
    
    def load_save_data(self, data):
        """Load from save data"""
        self.level = data.get("level", 1)
        self.xp = data.get("xp", 0)
        self.skill_points = data.get("skill_points", 0)
        self.skills = data.get("skills", self.skills)
        self.abilities = data.get("abilities", self.abilities)
        
        stats = data.get("stats", {})
        self.total_distance = stats.get("total_distance", 0)
        self.total_jumps = stats.get("total_jumps", 0)
        self.total_boosts = stats.get("total_boosts", 0)
        self.enemies_dodged = stats.get("enemies_dodged", 0)
        self.coins_collected = stats.get("coins_collected", 0)
        
        # Reapply all skill effects
        for skill_name in self.skills:
            self.apply_skill_effects(skill_name)


class AnimatedPlayer:
    """Advanced player with animations and physics"""
    
    def __init__(self):
        # Position
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.width, self.height = 140, 90  # Larger for detail
        
        # Physics
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.on_ground = True
        self.can_jump = True
        self.jumps_used = 0
        self.max_jumps = 1
        
        # Character stats
        self.stats = CharacterStats()
        
        # Animation
        self.current_animation = "idle"
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.1
        self.animations = {}
        
        # Powerups
        self.has_shield = False
        self.shield_timer = 0
        self.boost_active = False
        self.boost_timer = 0
        
        # Visual effects
        self.particles = []
        
        # Collision
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # Load animations
        self.load_animations()
    
    def load_animations(self):
        """Load sprite animations"""
        try:
            # First try to load the sprite with real character
            real_char_sprite = pygame.image.load("assets/images/player/player_with_real_character.png").convert_alpha()
            real_char_sprite = pygame.transform.scale(real_char_sprite, (self.width, self.height))
            # Use the real character for all animations (static for now)
            self.animations = {
                "idle": [real_char_sprite],
                "run": [real_char_sprite],
                "jump": [real_char_sprite],
                "boost": [real_char_sprite]
            }
            print("✅ Loaded player with real character image!")
        except:
            try:
                # Try to load animated sprite sheets
                animation_names = ["idle", "run", "jump", "boost"]
                for anim_name in animation_names:
                    sheet = pygame.image.load(f"assets/images/player/animations/{anim_name}.png").convert_alpha()
                    
                    # Parse sprite sheet (8 frames for most, 4 for jump)
                    frame_count = 4 if anim_name == "jump" else 8
                    frame_width = sheet.get_width() // frame_count
                    frame_height = sheet.get_height()
                    
                    frames = []
                    for i in range(frame_count):
                        frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
                        frame = pygame.transform.scale(frame, (self.width, self.height))
                        frames.append(frame)
                    
                    self.animations[anim_name] = frames
                print("✅ Loaded animated sprites")
            except Exception as e:
                print(f"Warning: Could not load animations: {e}")
                # Create fallback sprite
                fallback = pygame.Surface((self.width, self.height))
                fallback.fill(CYAN)
                self.animations = {"idle": [fallback]}
    
    def update(self, dt):
        """Update player with physics and animations"""
        # Energy regeneration
        self.stats.regen_energy(dt)
        
        # Update timers
        if self.boost_active:
            self.boost_timer -= dt
            if self.boost_timer <= 0:
                self.boost_active = False
                self.boost_timer = 0
        
        if self.has_shield:
            self.shield_timer -= dt
            if self.shield_timer <= 0:
                self.has_shield = False
                self.shield_timer = 0
        
        # Apply gravity
        if not self.on_ground:
            self.velocity_y += GRAVITY * dt
        
        # Apply movement
        self.y += self.velocity_y * dt
        self.x += self.velocity_x * dt
        
        # Ground collision
        ground_level = SCREEN_HEIGHT - GROUND_HEIGHT - self.height
        if self.y >= ground_level:
            self.y = ground_level
            self.velocity_y = 0
            self.on_ground = True
            self.can_jump = True
            self.jumps_used = 0
        else:
            self.on_ground = False
        
        # Update collision rect
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Determine animation
        self.update_animation(dt)
        
        # Update particles
        self.update_particles(dt)
    
    def update_animation(self, dt):
        """Update animation frame"""
        # Choose animation based on state
        if not self.on_ground:
            new_anim = "jump"
        elif self.boost_active:
            new_anim = "boost"
        elif abs(self.velocity_x) > 0.1:
            new_anim = "run"
        else:
            new_anim = "idle"
        
        # Reset frame if animation changed
        if new_anim != self.current_animation:
            self.current_animation = new_anim
            self.animation_frame = 0
            self.animation_timer = 0
        
        # Update frame timer
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            if self.current_animation in self.animations:
                frame_count = len(self.animations[self.current_animation])
                self.animation_frame = (self.animation_frame + 1) % frame_count
    
    def jump(self):
        """Perform jump"""
        # Check if can jump
        max_jumps = 2 if self.stats.abilities["double_jump"] else 1
        
        if self.jumps_used < max_jumps:
            self.velocity_y = -self.stats.jump_power
            self.on_ground = False
            self.jumps_used += 1
            self.stats.total_jumps += 1
            
            # Create jump particles
            self.create_jump_particles()
            return True
        return False
    
    def activate_boost(self):
        """Activate boost"""
        boost_cost = 20
        if self.stats.use_energy(boost_cost):
            self.boost_active = True
            self.boost_timer = 2.0 + (self.stats.skills["boost"]["level"] * 0.2)
            self.stats.total_boosts += 1
            return True
        return False
    
    def activate_shield(self):
        """Activate shield powerup"""
        self.has_shield = True
        duration = SHIELD_DURATION + (self.stats.skills["shield"]["level"] * 0.5)
        self.shield_timer = duration
    
    def create_jump_particles(self):
        """Create particle effect for jumping"""
        for _ in range(5):
            particle = {
                "x": self.x + self.width // 2,
                "y": self.y + self.height,
                "vx": random.uniform(-50, 50),
                "vy": random.uniform(-100, -50),
                "life": 0.5,
                "color": (200, 200, 200)
            }
            self.particles.append(particle)
    
    def update_particles(self, dt):
        """Update particle effects"""
        for particle in self.particles[:]:
            particle["x"] += particle["vx"] * dt
            particle["y"] += particle["vy"] * dt
            particle["vy"] += 500 * dt  # Gravity
            particle["life"] -= dt
            
            if particle["life"] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        """Draw player with current animation"""
        # Draw particles
        for particle in self.particles:
            alpha = int(255 * (particle["life"] / 0.5))
            color = (*particle["color"], alpha)
            pygame.draw.circle(screen, particle["color"], 
                             (int(particle["x"]), int(particle["y"])), 3)
        
        # Draw animated sprite
        if self.current_animation in self.animations:
            frame = self.animations[self.current_animation][self.animation_frame]
            screen.blit(frame, (self.x, self.y))
        
        # Draw shield effect
        if self.has_shield:
            shield_radius = max(self.width, self.height) // 2 + 10
            for i in range(3):
                alpha = int(100 - i * 30)
                pygame.draw.circle(screen, (0, 255, 255), 
                                 (int(self.x + self.width // 2), 
                                  int(self.y + self.height // 2)), 
                                 shield_radius + i * 3, 2)
        
        # Draw boost trail
        if self.boost_active:
            trail_length = 5
            for i in range(trail_length):
                alpha = int(200 - i * 40)
                offset = i * 15
                trail_rect = pygame.Rect(self.x - offset, self.y + 20, 20, 30)
                pygame.draw.ellipse(screen, (255, 200, 100), trail_rect)
    
    def reset(self):
        """Reset player for new game"""
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = True
        self.can_jump = True
        self.jumps_used = 0
        self.has_shield = False
        self.shield_timer = 0
        self.boost_active = False
        self.boost_timer = 0
        self.particles = []
        self.stats.energy = self.stats.max_energy
