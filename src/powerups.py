"""
Powerups: Energy orbs, boost, shields
"""

import pygame
import random
from src.settings import *

class Powerup:
    """Base powerup class"""
    
    def __init__(self, x, y, powerup_type):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.type = powerup_type
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.active = True
        self.pulse_time = 0
    
    def update(self, dt, scroll_speed):
        """Update powerup position"""
        self.x -= scroll_speed * dt
        self.rect.x = self.x
        self.pulse_time += dt
        
        if self.x + self.width < 0:
            self.active = False
    
    def draw(self, screen):
        """Draw powerup with pulsing effect"""
        pulse = abs(pygame.math.Vector2(1, 0).rotate(self.pulse_time * 360).x) * 5
        size = int(self.width + pulse)
        
        try:
            # Try to load generated sprites
            if self.type == "orb":
                sprite = pygame.image.load("assets/images/powerups/energy_orb.png").convert_alpha()
            else:  # shield
                sprite = pygame.image.load("assets/images/powerups/shield.png").convert_alpha()
            
            sprite = pygame.transform.scale(sprite, (size, size))
            screen.blit(sprite, (int(self.x + self.width // 2 - size // 2), 
                                int(self.y + self.height // 2 - size // 2)))
        except:
            # Fallback to procedural drawing
            if self.type == "orb":
                pygame.draw.circle(screen, YELLOW, 
                                 (int(self.x + self.width // 2), int(self.y + self.height // 2)), 
                                 size // 2)
                pygame.draw.circle(screen, WHITE, 
                                 (int(self.x + self.width // 2), int(self.y + self.height // 2)), 
                                 size // 4)
            
            elif self.type == "shield":
                pygame.draw.circle(screen, CYAN, 
                                 (int(self.x + self.width // 2), int(self.y + self.height // 2)), 
                                 size // 2, 3)
                pygame.draw.circle(screen, BLUE, 
                                 (int(self.x + self.width // 2), int(self.y + self.height // 2)), 
                                 size // 3, 2)

class PowerupManager:
    """Manages all powerups"""
    
    def __init__(self):
        self.powerups = []
    
    def spawn_powerup(self):
        """Spawn a new powerup"""
        x = SCREEN_WIDTH + random.randint(50, 150)
        y = random.randint(100, SCREEN_HEIGHT - GROUND_HEIGHT - 100)
        
        # Random powerup type (more orbs than shields)
        powerup_type = random.choice(["orb", "orb", "orb", "shield"])
        
        powerup = Powerup(x, y, powerup_type)
        self.powerups.append(powerup)
    
    def update(self, dt, scroll_speed):
        """Update all powerups"""
        for powerup in self.powerups:
            powerup.update(dt, scroll_speed)
        
        self.powerups = [p for p in self.powerups if p.active]
    
    def draw(self, screen):
        """Draw all powerups"""
        for powerup in self.powerups:
            powerup.draw(screen)
    
    def check_collision(self, player):
        """Check collision with player"""
        for powerup in self.powerups:
            if powerup.active and player.rect.colliderect(powerup.rect):
                powerup.active = False
                
                result = {"type": powerup.type, "score": 0}
                if powerup.type == "orb":
                    result["score"] = ORB_SCORE
                
                return result
        return None
    
    def clear(self):
        """Clear all powerups"""
        self.powerups.clear()
