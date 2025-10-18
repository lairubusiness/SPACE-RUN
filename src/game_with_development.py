"""
Complete Game with Advanced Character Development System
"""

import pygame
import random
from src.settings import *
from src.character_development import AnimatedPlayer, CharacterStats
from src.upgrade_ui import UpgradeUI, ParticleSystem
from src.background import Background
from src.enemy import EnemyManager
from src.powerups import PowerupManager
from src.ui import UI
from src.save_load import SaveManager
from src.landing_page import LandingPage

class AdvancedGame:
    """Main game with full character development"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE + " - Character Development Edition")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.state = "MENU"  # MENU, PLAYING, PAUSED, UPGRADE, GAME_OVER
        self.running = True
        
        # Game components
        self.player = AnimatedPlayer()
        self.background = Background()
        self.enemy_manager = EnemyManager()
        self.powerup_manager = PowerupManager()
        self.ui = UI()
        self.upgrade_ui = UpgradeUI()
        self.particles = ParticleSystem()
        self.save_manager = SaveManager()
        self.landing_page = LandingPage()
        
        # Game variables
        self.score = 0
        self.distance = 0
        self.high_score = 0
        self.scroll_speed = SCROLL_SPEED
        self.spawn_timer = 0
        self.powerup_timer = 0
        
        # Load saved data
        self.load_game_data()
    
    def load_game_data(self):
        """Load saved game data"""
        data = self.save_manager.load()
        self.high_score = data.get("high_score", 0)
        player_data = data.get("player_stats", {})
        if player_data:
            self.player.stats.load_save_data(player_data)
    
    def save_game_data(self):
        """Save game data"""
        data = {
            "high_score": self.high_score,
            "player_stats": self.player.stats.get_save_data()
        }
        self.save_manager.save(data)
    
    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()
    
    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if self.state == "MENU":
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                    elif event.key == pygame.K_u:
                        self.state = "UPGRADE"
                
                elif self.state == "PLAYING":
                    if event.key == pygame.K_SPACE:
                        if self.player.jump():
                            # Create jump particles
                            self.particles.emit(
                                self.player.x + self.player.width // 2,
                                self.player.y + self.player.height,
                                8, "default"
                            )
                    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        if self.player.activate_boost():
                            pass  # Boost activated
                    elif event.key == pygame.K_ESCAPE:
                        self.state = "PAUSED"
                    elif event.key == pygame.K_u:
                        self.state = "UPGRADE"
                
                elif self.state == "PAUSED":
                    if event.key == pygame.K_ESCAPE:
                        self.state = "PLAYING"
                    elif event.key == pygame.K_q:
                        self.state = "MENU"
                
                elif self.state == "UPGRADE":
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_u:
                        if self.state != "MENU":
                            self.state = "PLAYING"
                        else:
                            self.state = "MENU"
                
                elif self.state == "GAME_OVER":
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.state = "MENU"
                    elif event.key == pygame.K_u:
                        self.state = "UPGRADE"
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "MENU":
                    action = self.landing_page.handle_click(event.pos)
                    if action == "start":
                        self.start_game()
                elif self.state == "UPGRADE":
                    result = self.upgrade_ui.handle_click(event.pos, self.player.stats)
                    if result:
                        # Play upgrade sound/effect
                        self.particles.emit(event.pos[0], event.pos[1], 15, "level_up")
                        self.save_game_data()
    
    def start_game(self):
        """Start a new game"""
        self.state = "PLAYING"
        self.score = 0
        self.distance = 0
        self.scroll_speed = SCROLL_SPEED
        self.player.reset()
        self.enemy_manager.clear()
        self.powerup_manager.clear()
        self.spawn_timer = 0
        self.powerup_timer = 0
    
    def update(self, dt):
        """Update game state"""
        # Update particles always
        self.particles.update(dt)
        
        # Update landing page animations
        if self.state == "MENU":
            self.landing_page.update(dt)
        
        if self.state == "PLAYING":
            # Update scroll speed
            self.scroll_speed = min(
                self.scroll_speed + SPEED_INCREASE_RATE * dt,
                MAX_SCROLL_SPEED
            )
            
            # Apply boost multiplier
            current_speed = self.scroll_speed
            if self.player.boost_active:
                current_speed *= self.player.stats.boost_power
                # Emit boost particles
                if random.random() > 0.5:
                    self.particles.emit(
                        self.player.x,
                        self.player.y + self.player.height // 2,
                        2, "boost"
                    )
            
            # Update distance
            self.distance += current_speed * dt
            self.player.stats.total_distance = int(self.distance)
            
            # Gain XP based on distance
            xp_gain = int(current_speed * dt * 0.1)
            if xp_gain > 0:
                levels = self.player.stats.gain_xp(xp_gain)
                if levels > 0:
                    # Level up effect!
                    self.particles.emit(
                        self.player.x + self.player.width // 2,
                        self.player.y + self.player.height // 2,
                        30, "level_up"
                    )
            
            # Update background
            self.background.update(dt, current_speed)
            
            # Update player
            self.player.update(dt)
            
            # Spawn enemies
            self.spawn_timer += dt
            if self.spawn_timer >= ENEMY_SPAWN_RATE:
                self.enemy_manager.spawn_enemy()
                self.spawn_timer = 0
            
            # Spawn powerups
            self.powerup_timer += dt
            if self.powerup_timer >= POWERUP_SPAWN_RATE:
                self.powerup_manager.spawn_powerup()
                self.powerup_timer = 0
            
            # Update enemies and powerups
            self.enemy_manager.update(dt, current_speed)
            self.powerup_manager.update(dt, current_speed)
            
            # Check collisions
            self.check_collisions()
    
    def check_collisions(self):
        """Check for collisions between game objects"""
        # Check enemy collisions
        if self.enemy_manager.check_collision(self.player):
            if not self.player.has_shield:
                self.game_over()
            else:
                self.player.has_shield = False
                self.player.shield_timer = 0
                self.player.stats.enemies_dodged += 1
        
        # Check powerup collisions with magnet effect
        magnet_range = 100 if self.player.stats.abilities["coin_magnet"] else 0
        
        collected = self.powerup_manager.check_collision(self.player)
        if collected:
            self.score += collected["score"]
            self.player.stats.coins_collected += 1
            
            if collected["type"] == "shield":
                self.player.activate_shield()
            
            # Particle effect
            self.particles.emit(
                self.player.x + self.player.width // 2,
                self.player.y + self.player.height // 2,
                10, "level_up"
            )
    
    def game_over(self):
        """Handle game over"""
        self.state = "GAME_OVER"
        if self.score > self.high_score:
            self.high_score = self.score
        
        # Bonus XP for score
        bonus_xp = self.score
        levels = self.player.stats.gain_xp(bonus_xp)
        if levels > 0:
            self.particles.emit(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 50, "level_up")
        
        self.save_game_data()
    
    def draw(self):
        """Render game objects"""
        # Draw background
        self.background.draw(self.screen)
        
        if self.state == "MENU":
            # Use enhanced landing page
            self.landing_page.draw(self.screen, self.high_score, self.player.stats.level)
        
        elif self.state == "PLAYING":
            # Draw game objects
            self.powerup_manager.draw(self.screen)
            self.enemy_manager.draw(self.screen)
            self.player.draw(self.screen)
            self.particles.draw(self.screen)
            
            # Draw HUD
            self.draw_hud()
        
        elif self.state == "PAUSED":
            # Draw game objects (frozen)
            self.powerup_manager.draw(self.screen)
            self.enemy_manager.draw(self.screen)
            self.player.draw(self.screen)
            
            # Draw pause overlay
            self.ui.draw_pause(self.screen)
        
        elif self.state == "UPGRADE":
            # Draw upgrade screen
            self.upgrade_ui.draw_upgrade_screen(self.screen, self.player.stats)
            self.particles.draw(self.screen)
        
        elif self.state == "GAME_OVER":
            self.draw_game_over()
        
        pygame.display.flip()
    
    def draw_menu(self):
        """Draw main menu"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        font_large = pygame.font.Font(None, 64)
        font_medium = pygame.font.Font(None, 36)
        font_small = pygame.font.Font(None, 28)
        
        # Title
        title = font_large.render("SPACE RUN", True, CYAN)
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 100))
        
        # Level info
        level_text = font_medium.render(f"Level {self.player.stats.level} Character", True, YELLOW)
        self.screen.blit(level_text, (SCREEN_WIDTH//2 - level_text.get_width()//2, 200))
        
        # Instructions
        instructions = [
            "Press SPACE to Start",
            "Press U for Upgrades",
            "",
            "Controls:",
            "SPACE - Jump",
            "SHIFT - Boost",
            "U - Upgrades (during game)",
        ]
        
        y_offset = 280
        for line in instructions:
            text = font_small.render(line, True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, y_offset))
            y_offset += 35
        
        # High score
        hs_text = font_medium.render(f"High Score: {self.high_score}", True, YELLOW)
        self.screen.blit(hs_text, (SCREEN_WIDTH//2 - hs_text.get_width()//2, SCREEN_HEIGHT - 80))
    
    def draw_hud(self):
        """Draw HUD during gameplay"""
        font_medium = pygame.font.Font(None, 32)
        font_small = pygame.font.Font(None, 24)
        
        # Score
        score_text = font_medium.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (20, 20))
        
        # Distance
        dist_text = font_medium.render(f"Distance: {int(self.distance)}m", True, WHITE)
        self.screen.blit(dist_text, (20, 55))
        
        # Level
        level_text = font_medium.render(f"Level: {self.player.stats.level}", True, YELLOW)
        self.screen.blit(level_text, (20, 90))
        
        # XP Bar (small)
        xp_ratio = self.player.stats.xp / self.player.stats.xp_to_next_level
        xp_bar_rect = pygame.Rect(20, 125, 200, 15)
        pygame.draw.rect(self.screen, (60, 60, 100), xp_bar_rect, border_radius=3)
        if xp_ratio > 0:
            fill_rect = pygame.Rect(xp_bar_rect.x, xp_bar_rect.y, 
                                   int(xp_bar_rect.width * xp_ratio), xp_bar_rect.height)
            pygame.draw.rect(self.screen, (100, 255, 100), fill_rect, border_radius=3)
        pygame.draw.rect(self.screen, CYAN, xp_bar_rect, 2, border_radius=3)
        
        # Energy Bar
        self.upgrade_ui.draw_energy_bar(self.screen, self.player.stats, 
                                       SCREEN_WIDTH - 220, 20, 200, 25)
        
        # Skill points indicator
        if self.player.stats.skill_points > 0:
            sp_text = font_small.render(f"[U] {self.player.stats.skill_points} Skill Points!", 
                                       True, YELLOW)
            # Pulsing effect
            import math
            alpha = int(200 + 55 * math.sin(pygame.time.get_ticks() * 0.005))
            sp_text.set_alpha(alpha)
            self.screen.blit(sp_text, (SCREEN_WIDTH - 220, 60))
    
    def draw_game_over(self):
        """Draw game over screen"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        font_large = pygame.font.Font(None, 64)
        font_medium = pygame.font.Font(None, 36)
        font_small = pygame.font.Font(None, 28)
        
        # Title
        title = font_large.render("GAME OVER", True, RED)
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 150))
        
        # Stats
        stats = [
            f"Score: {self.score}",
            f"Distance: {int(self.distance)}m",
            f"Level: {self.player.stats.level}",
            f"High Score: {self.high_score}",
        ]
        
        y_offset = 260
        for stat in stats:
            text = font_medium.render(stat, True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, y_offset))
            y_offset += 45
        
        # Instructions
        instructions = [
            "Press SPACE to Restart",
            "Press U for Upgrades",
            "Press ESC for Menu",
        ]
        
        y_offset += 30
        for line in instructions:
            text = font_small.render(line, True, CYAN)
            self.screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, y_offset))
            y_offset += 35
        
        # Particles
        self.particles.draw(self.screen)


if __name__ == "__main__":
    game = AdvancedGame()
    game.run()
