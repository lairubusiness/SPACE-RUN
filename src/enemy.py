"""
Enemy obstacles and UFO logic
"""

import pygame
import random
from src.settings import *

class Enemy:
    """Base enemy class"""
    
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
        self.active = True
    
    def update(self, dt, scroll_speed):
        """Update enemy position"""
        self.x -= (scroll_speed + self.speed) * dt
        self.rect.x = self.x
        
        # Deactivate if off screen
        if self.x + self.width < 0:
            self.active = False
    
    def draw(self, screen):
        """Draw enemy (to be overridden)"""
        pass

class Asteroid(Enemy):
    """Asteroid obstacle"""
    
    def __init__(self, x, y):
        size = random.randint(40, 80)
        speed = random.randint(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX)
        super().__init__(x, y, size, size, speed)
        self.rotation = random.randint(0, 360)
        self.rotation_speed = random.randint(-100, 100)
        self.create_sprite()
    
    def create_sprite(self):
        """Load or create asteroid sprite"""
        try:
            # Load random asteroid sprite
            asteroid_num = random.randint(1, 4)
            self.sprite = pygame.image.load(f"assets/images/enemies/asteroid_{asteroid_num}.png").convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        except:
            # Fallback to procedural generation
            self.sprite = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            points = []
            for i in range(8):
                angle = i * 45
                radius = self.width // 2 * random.uniform(0.7, 1.0)
                x = self.width // 2 + radius * pygame.math.Vector2(1, 0).rotate(angle).x
                y = self.height // 2 + radius * pygame.math.Vector2(1, 0).rotate(angle).y
                points.append((x, y))
            pygame.draw.polygon(self.sprite, (150, 75, 0), points)
    
    def update(self, dt, scroll_speed):
        """Update asteroid"""
        super().update(dt, scroll_speed)
        self.rotation += self.rotation_speed * dt
    
    def draw(self, screen):
        """Draw rotating asteroid"""
        rotated = pygame.transform.rotate(self.sprite, self.rotation)
        rect = rotated.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(rotated, rect)

class UFO(Enemy):
    """UFO enemy that moves in wave pattern"""
    
    def __init__(self, x, y):
        super().__init__(x, y, 60, 40, UFO_SPEED)
        self.start_y = y
        self.wave_amplitude = 50
        self.wave_frequency = 2.0
        self.time = 0
        self.create_sprite()
    
    def create_sprite(self):
        """Load or create UFO sprite"""
        try:
            # Load generated UFO sprite
            self.sprite = pygame.image.load("assets/images/enemies/ufo.png").convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        except:
            # Fallback to procedural generation
            self.sprite = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.ellipse(self.sprite, (100, 200, 100), (5, 15, 50, 20))
            pygame.draw.ellipse(self.sprite, (150, 255, 150), (15, 5, 30, 20))
            pygame.draw.circle(self.sprite, (255, 255, 0), (30, 15), 5)
    
    def update(self, dt, scroll_speed):
        """Update UFO with wave motion"""
        super().update(dt, scroll_speed)
        self.time += dt
        self.y = self.start_y + self.wave_amplitude * pygame.math.Vector2(0, 1).rotate(
            self.time * self.wave_frequency * 360
        ).y
        self.rect.y = self.y
    
    def draw(self, screen):
        """Draw UFO"""
        screen.blit(self.sprite, (self.x, self.y))

class EnemyManager:
    """Manages all enemies"""
    
    def __init__(self):
        self.enemies = []
        self.last_spawn_x = SCREEN_WIDTH
    
    def spawn_enemy(self):
        """Spawn a new enemy"""
        # Random spawn position
        x = SCREEN_WIDTH + random.randint(50, 200)
        
        # Ensure minimum gap
        if x - self.last_spawn_x < ENEMY_MIN_GAP:
            x = self.last_spawn_x + ENEMY_MIN_GAP
        
        self.last_spawn_x = x
        
        # Choose enemy type
        enemy_type = random.choice(["asteroid", "asteroid", "ufo"])  # More asteroids
        
        if enemy_type == "asteroid":
            y = SCREEN_HEIGHT - GROUND_HEIGHT - random.randint(50, 200)
            enemy = Asteroid(x, y)
        else:
            y = random.randint(100, SCREEN_HEIGHT - GROUND_HEIGHT - 150)
            enemy = UFO(x, y)
        
        self.enemies.append(enemy)
    
    def update(self, dt, scroll_speed):
        """Update all enemies"""
        for enemy in self.enemies:
            enemy.update(dt, scroll_speed)
        
        # Remove inactive enemies
        self.enemies = [e for e in self.enemies if e.active]
    
    def draw(self, screen):
        """Draw all enemies"""
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def check_collision(self, player):
        """Check collision with player"""
        for enemy in self.enemies:
            if enemy.active and player.rect.colliderect(enemy.rect):
                enemy.active = False
                return True
        return False
    
    def clear(self):
        """Clear all enemies"""
        self.enemies.clear()
        self.last_spawn_x = SCREEN_WIDTH
