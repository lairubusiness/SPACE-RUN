"""
Parallax background scrolling system
"""

import pygame
from src.settings import *

class Background:
    """Manages parallax scrolling background"""
    
    def __init__(self):
        # Create layers
        self.create_space_background()
        self.create_star_layers()
        
        # Scroll positions
        self.bg_scroll = 0
        self.star_scroll_1 = 0
        self.star_scroll_2 = 0
    
    def create_space_background(self):
        """Load or create main space background"""
        try:
            # Load generated space background
            self.bg_surface = pygame.image.load("assets/images/backgrounds/space_bg.png").convert()
            self.bg_surface = pygame.transform.scale(self.bg_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            # Fallback to procedural gradient
            self.bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            for y in range(SCREEN_HEIGHT):
                ratio = y / SCREEN_HEIGHT
                r = int(10 + (50 - 10) * ratio)
                g = int(10 + (20 - 10) * ratio)
                b = int(50 + (80 - 50) * ratio)
                pygame.draw.line(self.bg_surface, (r, g, b), (0, y), (SCREEN_WIDTH, y))
    
    def create_star_layers(self):
        """Load or create star layers for parallax effect"""
        import random
        
        try:
            # Load generated stars
            stars = pygame.image.load("assets/images/backgrounds/stars_layer.png").convert_alpha()
            self.stars_layer_1 = pygame.transform.scale(stars, (SCREEN_WIDTH * 2, SCREEN_HEIGHT))
            self.stars_layer_2 = self.stars_layer_1.copy()
        except:
            # Fallback to procedural generation
            # Layer 1 - Distant stars (slow)
            self.stars_layer_1 = pygame.Surface((SCREEN_WIDTH * 2, SCREEN_HEIGHT), pygame.SRCALPHA)
            for _ in range(100):
                x = random.randint(0, SCREEN_WIDTH * 2)
                y = random.randint(0, SCREEN_HEIGHT - GROUND_HEIGHT)
                size = random.randint(1, 2)
                brightness = random.randint(100, 200)
                pygame.draw.circle(
                    self.stars_layer_1, 
                    (brightness, brightness, brightness), 
                    (x, y), 
                    size
                )
            
            # Layer 2 - Close stars (faster)
            self.stars_layer_2 = pygame.Surface((SCREEN_WIDTH * 2, SCREEN_HEIGHT), pygame.SRCALPHA)
            for _ in range(50):
                x = random.randint(0, SCREEN_WIDTH * 2)
                y = random.randint(0, SCREEN_HEIGHT - GROUND_HEIGHT)
                size = random.randint(2, 3)
                brightness = random.randint(150, 255)
                pygame.draw.circle(
                    self.stars_layer_2, 
                    (brightness, brightness, brightness), 
                    (x, y), 
                    size
                )
        
        # Add floating planets to star layer
        self.add_planets_to_background()
    
    def add_planets_to_background(self):
        """Add decorative planets to background"""
        import random
        try:
            planet_types = ['planet_blue', 'planet_red', 'planet_purple', 'planet_pink']
            for _ in range(4):
                planet_type = random.choice(planet_types)
                planet = pygame.image.load(f"assets/images/backgrounds/{planet_type}.png").convert_alpha()
                size = random.randint(40, 80)
                planet = pygame.transform.scale(planet, (size, size))
                x = random.randint(0, SCREEN_WIDTH * 2 - size)
                y = random.randint(50, SCREEN_HEIGHT - GROUND_HEIGHT - size - 50)
                self.stars_layer_1.blit(planet, (x, y))
        except:
            pass  # Skip if planets not found
    
    def update(self, dt, scroll_speed):
        """Update scrolling positions"""
        # Parallax effect - different layers move at different speeds
        self.star_scroll_1 += scroll_speed * 0.2 * dt
        self.star_scroll_2 += scroll_speed * 0.5 * dt
        
        # Wrap around
        if self.star_scroll_1 >= SCREEN_WIDTH:
            self.star_scroll_1 = 0
        if self.star_scroll_2 >= SCREEN_WIDTH:
            self.star_scroll_2 = 0
    
    def draw(self, screen):
        """Draw all background layers"""
        # Draw main background
        screen.blit(self.bg_surface, (0, 0))
        
        # Draw star layers with parallax
        screen.blit(self.stars_layer_1, (-self.star_scroll_1, 0))
        screen.blit(self.stars_layer_2, (-self.star_scroll_2, 0))
        
        # Draw ground
        try:
            # Try to load grid ground
            grid_ground = pygame.image.load("assets/images/backgrounds/grid_ground.png").convert_alpha()
            grid_ground = pygame.transform.scale(grid_ground, (SCREEN_WIDTH, GROUND_HEIGHT))
            screen.blit(grid_ground, (0, SCREEN_HEIGHT - GROUND_HEIGHT))
        except:
            # Fallback to simple ground
            ground_rect = pygame.Rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT)
            pygame.draw.rect(screen, (60, 60, 80), ground_rect)
            pygame.draw.line(screen, (80, 80, 100), (0, SCREEN_HEIGHT - GROUND_HEIGHT), 
                            (SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT), 3)
