"""
Player character logic and progression system
"""

import pygame
from src.settings import *

class Player:
    """Chibi character with hover-car"""
    
    def __init__(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.width, self.height = PLAYER_SIZE
        
        # Physics
        self.velocity_y = 0
        self.is_jumping = False
        self.on_ground = True
        
        # Powerups
        self.has_shield = False
        self.shield_timer = 0
        self.boost_active = False
        self.boost_timer = 0
        
        # Animation
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.1  # Seconds per frame
        
        # Stats (for progression)
        self.level = 1
        self.experience = 0
        self.upgrades = {
            "jump_power": 0,
            "boost_duration": 0,
            "shield_duration": 0
        }
        
        # Create rect for collision
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # Placeholder surface (will be replaced with sprites)
        self.create_placeholder_sprite()
    
    def create_placeholder_sprite(self):
        """Load sprite with real character image"""
        try:
            # Try to load the sprite with real character
            self.sprite = pygame.image.load("assets/images/player/player_with_real_character.png").convert_alpha()
            # Scale to match player size
            self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
            print("✅ Loaded player sprite with real character!")
        except:
            try:
                # Fallback to generated sprite
                self.sprite = pygame.image.load("assets/images/player/car.png").convert_alpha()
                self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
                print("✅ Loaded generated player sprite")
            except:
                # Final fallback to simple placeholder
                self.sprite = pygame.Surface((self.width, self.height))
                self.sprite.fill(CYAN)
                pygame.draw.rect(self.sprite, BLUE, (10, 20, 60, 40))
                pygame.draw.circle(self.sprite, BLACK, (25, 60), 10)
                pygame.draw.circle(self.sprite, BLACK, (55, 60), 10)
                print("⚠️ Using placeholder sprite")
    
    def jump(self):
        """Make the player jump"""
        if self.on_ground:
            jump_power = PLAYER_JUMP_VELOCITY - (self.upgrades["jump_power"] * 50)
            self.velocity_y = jump_power
            self.is_jumping = True
            self.on_ground = False
    
    def activate_boost(self):
        """Activate speed boost"""
        if not self.boost_active:
            self.boost_active = True
            duration = PLAYER_BOOST_DURATION + (self.upgrades["boost_duration"] * 0.5)
            self.boost_timer = duration
    
    def activate_shield(self):
        """Activate shield powerup"""
        self.has_shield = True
        duration = SHIELD_DURATION + (self.upgrades["shield_duration"] * 1.0)
        self.shield_timer = duration
    
    def remove_shield(self):
        """Remove shield after taking damage"""
        self.has_shield = False
        self.shield_timer = 0
    
    def update(self, dt):
        """Update player state"""
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
        
        # Update position
        self.y += self.velocity_y * dt
        
        # Check ground collision
        ground_level = SCREEN_HEIGHT - GROUND_HEIGHT - self.height
        if self.y >= ground_level:
            self.y = ground_level
            self.velocity_y = 0
            self.is_jumping = False
            self.on_ground = True
        
        # Update rect for collision detection
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Update animation
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_frame = (self.animation_frame + 1) % 4
            self.animation_timer = 0
    
    def draw(self, screen):
        """Draw the player"""
        # Draw player sprite
        screen.blit(self.sprite, (self.x, self.y))
        
        # Draw shield effect
        if self.has_shield:
            pygame.draw.circle(
                screen, 
                (0, 255, 255, 128), 
                (int(self.x + self.width // 2), int(self.y + self.height // 2)), 
                self.width // 2 + 10,
                3
            )
        
        # Draw boost effect
        if self.boost_active:
            flame_rect = pygame.Rect(self.x - 20, self.y + 20, 20, 40)
            pygame.draw.ellipse(screen, YELLOW, flame_rect)
    
    def get_stats(self):
        """Get player stats for saving"""
        return {
            "level": self.level,
            "experience": self.experience,
            "upgrades": self.upgrades
        }
    
    def load_stats(self, stats):
        """Load player stats from save data"""
        self.level = stats.get("level", 1)
        self.experience = stats.get("experience", 0)
        self.upgrades = stats.get("upgrades", {
            "jump_power": 0,
            "boost_duration": 0,
            "shield_duration": 0
        })
    
    def reset(self):
        """Reset player position and state for new game"""
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.velocity_y = 0
        self.is_jumping = False
        self.on_ground = True
        self.has_shield = False
        self.shield_timer = 0
        self.boost_active = False
        self.boost_timer = 0
