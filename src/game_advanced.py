"""
Core game loop and state management
"""

import pygame
from src.settings import *
from src.player import Player
from src.enemy import EnemyManager
from src.background import Background
from src.ui import UI
from src.powerups import PowerupManager
from src.save_load import SaveManager

class Game:
    """Main game class that handles game loop and state"""
    
    def __init__(self, screen):
        self.screen = screen
        self.state = "MENU"  # MENU, PLAYING, PAUSED, GAME_OVER
        self.score = 0
        self.distance = 0
        self.high_score = 0
        
        # Game components
        self.background = Background()
        self.player = Player()
        self.enemy_manager = EnemyManager()
        self.powerup_manager = PowerupManager()
        self.ui = UI()
        self.save_manager = SaveManager()
        
        # Load saved data
        self.load_game_data()
        
        # Game variables
        self.scroll_speed = SCROLL_SPEED
        self.spawn_timer = 0
        self.powerup_timer = 0
    
    def load_game_data(self):
        """Load saved game data"""
        data = self.save_manager.load()
        self.high_score = data.get("high_score", 0)
        self.player.load_stats(data.get("player_stats", {}))
    
    def save_game_data(self):
        """Save game data"""
        data = {
            "high_score": self.high_score,
            "player_stats": self.player.get_stats()
        }
        self.save_manager.save(data)
    
    def handle_events(self, event):
        """Handle game events"""
        if self.state == "MENU":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_game()
        
        elif self.state == "PLAYING":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                elif event.key == pygame.K_LSHIFT:
                    self.player.activate_boost()
                elif event.key == pygame.K_ESCAPE:
                    self.state = "PAUSED"
        
        elif self.state == "PAUSED":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = "PLAYING"
                elif event.key == pygame.K_q:
                    self.state = "MENU"
        
        elif self.state == "GAME_OVER":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_game()
                elif event.key == pygame.K_ESCAPE:
                    self.state = "MENU"
    
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
        if self.state == "PLAYING":
            # Update scroll speed
            self.scroll_speed = min(
                self.scroll_speed + SPEED_INCREASE_RATE * dt,
                MAX_SCROLL_SPEED
            )
            
            # Update distance
            self.distance += self.scroll_speed * dt
            
            # Update background
            self.background.update(dt, self.scroll_speed)
            
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
            self.enemy_manager.update(dt, self.scroll_speed)
            self.powerup_manager.update(dt, self.scroll_speed)
            
            # Check collisions
            self.check_collisions()
    
    def check_collisions(self):
        """Check for collisions between game objects"""
        # Check enemy collisions
        if self.enemy_manager.check_collision(self.player):
            if not self.player.has_shield:
                self.game_over()
            else:
                self.player.remove_shield()
        
        # Check powerup collisions
        collected = self.powerup_manager.check_collision(self.player)
        if collected:
            self.score += collected["score"]
            if collected["type"] == "shield":
                self.player.activate_shield()
    
    def game_over(self):
        """Handle game over"""
        self.state = "GAME_OVER"
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_game_data()
    
    def draw(self):
        """Render game objects"""
        # Draw background
        self.background.draw(self.screen)
        
        if self.state == "MENU":
            self.ui.draw_menu(self.screen, self.high_score)
        
        elif self.state == "PLAYING":
            # Draw game objects
            self.powerup_manager.draw(self.screen)
            self.enemy_manager.draw(self.screen)
            self.player.draw(self.screen)
            
            # Draw HUD
            self.ui.draw_hud(self.screen, self.score, int(self.distance), self.player)
        
        elif self.state == "PAUSED":
            # Draw game objects (frozen)
            self.powerup_manager.draw(self.screen)
            self.enemy_manager.draw(self.screen)
            self.player.draw(self.screen)
            
            # Draw pause overlay
            self.ui.draw_pause(self.screen)
        
        elif self.state == "GAME_OVER":
            self.ui.draw_game_over(self.screen, self.score, self.high_score)
