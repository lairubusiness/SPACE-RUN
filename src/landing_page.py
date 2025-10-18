"""
Advanced Landing Page with Animated Space Theme
Features orbiting elements around character icon
"""

import pygame
import math
import random
from src.settings import *

class LandingPage:
    """Enhanced landing/menu page with animations"""
    
    def __init__(self):
        pygame.font.init()
        self.font_title = pygame.font.Font(None, 84)
        self.font_large = pygame.font.Font(None, 64)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 28)
        
        # Load character icon
        self.load_character_icon()
        
        # Animation variables
        self.time = 0
        self.title_pulse = 0
        self.start_button_pulse = 0
        
        # Orbiting elements
        self.create_orbiting_elements()
        
        # Particle stars
        self.stars = []
        self.create_star_field()
        
        # Interactive state
        self.buttons = {}
        self.hovered_button = None
    
    def load_character_icon(self):
        """Load the astronaut character icon"""
        try:
            icon = pygame.image.load("C:/Users/LENOVO/Downloads/SPACE_GAME/IMAGE/Gemini_Generated_Image_sjanu9sjanu9sjan.png").convert_alpha()
            # Scale to appropriate size (keep aspect ratio)
            target_size = 300
            icon = pygame.transform.scale(icon, (target_size, target_size))
            self.character_icon = icon
            self.icon_size = target_size
        except Exception as e:
            print(f"Could not load character icon: {e}")
            # Create fallback
            self.icon_size = 200
            self.character_icon = pygame.Surface((self.icon_size, self.icon_size), pygame.SRCALPHA)
            pygame.draw.circle(self.character_icon, CYAN, 
                             (self.icon_size//2, self.icon_size//2), self.icon_size//2)
    
    def create_orbiting_elements(self):
        """Create elements that orbit around the character"""
        self.orbit_elements = []
        
        # Create various space objects
        orbit_configs = [
            {"distance": 180, "speed": 1.0, "size": 20, "color": (255, 200, 100), "type": "star"},
            {"distance": 200, "speed": -0.8, "size": 15, "color": (100, 200, 255), "type": "planet"},
            {"distance": 220, "speed": 1.2, "size": 12, "color": (255, 150, 200), "type": "star"},
            {"distance": 240, "speed": -1.5, "size": 18, "color": (150, 255, 150), "type": "planet"},
            {"distance": 260, "speed": 0.9, "size": 10, "color": (200, 200, 255), "type": "star"},
            {"distance": 170, "speed": -1.8, "size": 14, "color": (255, 255, 100), "type": "ufo"},
        ]
        
        for i, config in enumerate(orbit_configs):
            element = {
                **config,
                "angle": i * 60  # Spread them out initially
            }
            self.orbit_elements.append(element)
    
    def create_star_field(self):
        """Create twinkling background stars"""
        for _ in range(100):
            star = {
                "x": random.randint(0, SCREEN_WIDTH),
                "y": random.randint(0, SCREEN_HEIGHT),
                "size": random.choice([1, 1, 2, 2, 3]),
                "brightness": random.randint(100, 255),
                "twinkle_speed": random.uniform(0.5, 2.0),
                "twinkle_offset": random.uniform(0, math.pi * 2)
            }
            self.stars.append(star)
    
    def update(self, dt):
        """Update animations"""
        self.time += dt
        
        # Update orbiting elements
        for element in self.orbit_elements:
            element["angle"] += element["speed"] * dt * 50  # Speed multiplier
            element["angle"] %= 360
        
        # Update pulsing effects
        self.title_pulse = abs(math.sin(self.time * 2))
        self.start_button_pulse = abs(math.sin(self.time * 3))
    
    def draw(self, screen, high_score=0, character_level=1):
        """Draw the complete landing page"""
        # Draw space background gradient
        self.draw_gradient_background(screen)
        
        # Draw twinkling stars
        self.draw_star_field(screen)
        
        # Center position for character
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2 - 50
        
        # Draw orbiting elements
        self.draw_orbiting_elements(screen, center_x, center_y)
        
        # Draw glow effect behind character
        self.draw_character_glow(screen, center_x, center_y)
        
        # Draw character icon
        icon_rect = self.character_icon.get_rect(center=(center_x, center_y))
        screen.blit(self.character_icon, icon_rect)
        
        # Draw orbital ring
        self.draw_orbital_ring(screen, center_x, center_y)
        
        # Draw title above
        self.draw_title(screen)
        
        # Draw menu options below
        self.draw_menu_options(screen, high_score, character_level)
        
        # Draw decorative elements
        self.draw_corner_decorations(screen)
    
    def draw_gradient_background(self, screen):
        """Draw animated gradient background"""
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            # Animated color shift
            color_shift = int(20 * math.sin(self.time * 0.5 + ratio * 2))
            r = max(0, min(255, int(10 + (60 - 10) * ratio + color_shift)))
            g = max(0, min(255, int(10 + (30 - 10) * ratio)))
            b = max(0, min(255, int(40 + (100 - 40) * ratio + color_shift)))
            pygame.draw.line(screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
    
    def draw_star_field(self, screen):
        """Draw twinkling stars"""
        for star in self.stars:
            # Twinkling effect
            twinkle = abs(math.sin(self.time * star["twinkle_speed"] + star["twinkle_offset"]))
            brightness = int(star["brightness"] * (0.5 + 0.5 * twinkle))
            color = (brightness, brightness, brightness)
            
            pygame.draw.circle(screen, color, (star["x"], star["y"]), star["size"])
            
            # Cross glow for larger stars
            if star["size"] >= 2 and twinkle > 0.7:
                glow_color = (*color, 100)
                pygame.draw.line(screen, color, 
                               (star["x"] - 4, star["y"]), 
                               (star["x"] + 4, star["y"]), 1)
                pygame.draw.line(screen, color, 
                               (star["x"], star["y"] - 4), 
                               (star["x"], star["y"] + 4), 1)
    
    def draw_character_glow(self, screen, x, y):
        """Draw glowing effect behind character"""
        # Multiple layers of glow
        for i in range(5, 0, -1):
            alpha = 30 * (6 - i)
            radius = self.icon_size // 2 + 20 + i * 10
            glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            
            # Pulsing glow
            pulse = abs(math.sin(self.time * 2))
            final_radius = int(radius * (0.9 + 0.1 * pulse))
            
            pygame.draw.circle(glow_surface, (100, 200, 255, alpha), 
                             (radius, radius), final_radius)
            screen.blit(glow_surface, 
                       (x - radius, y - radius), 
                       special_flags=pygame.BLEND_ALPHA_SDL2)
    
    def draw_orbiting_elements(self, screen, center_x, center_y):
        """Draw orbiting planets and stars"""
        for element in self.orbit_elements:
            angle_rad = math.radians(element["angle"])
            x = center_x + int(math.cos(angle_rad) * element["distance"])
            y = center_y + int(math.sin(angle_rad) * element["distance"])
            
            # Draw based on type
            if element["type"] == "star":
                self.draw_star_element(screen, x, y, element)
            elif element["type"] == "planet":
                self.draw_planet_element(screen, x, y, element)
            elif element["type"] == "ufo":
                self.draw_ufo_element(screen, x, y, element)
    
    def draw_star_element(self, screen, x, y, element):
        """Draw a star in the orbit"""
        size = element["size"]
        color = element["color"]
        
        # Draw star with glow
        pygame.draw.circle(screen, color, (x, y), size)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), size // 2)
        
        # Star points
        for i in range(4):
            angle = i * 90 + self.time * 100
            length = size + 3
            x1 = x + int(math.cos(math.radians(angle)) * length)
            y1 = y + int(math.sin(math.radians(angle)) * length)
            pygame.draw.line(screen, color, (x, y), (x1, y1), 2)
    
    def draw_planet_element(self, screen, x, y, element):
        """Draw a mini planet"""
        size = element["size"]
        color = element["color"]
        
        # Planet body
        pygame.draw.circle(screen, color, (x, y), size)
        
        # Highlight
        highlight_x = x - size // 3
        highlight_y = y - size // 3
        pygame.draw.circle(screen, (255, 255, 255, 100), 
                         (highlight_x, highlight_y), size // 3)
        
        # Ring (for some planets)
        if element["distance"] % 80 == 0:
            ring_rect = pygame.Rect(x - size * 1.5, y - size // 3, size * 3, size * 0.6)
            pygame.draw.ellipse(screen, (*color, 150), ring_rect, 2)
    
    def draw_ufo_element(self, screen, x, y, element):
        """Draw a tiny UFO"""
        size = element["size"]
        
        # UFO body
        ufo_points = [
            (x - size, y),
            (x - size // 2, y - size // 2),
            (x + size // 2, y - size // 2),
            (x + size, y),
            (x + size // 2, y + size // 3),
            (x - size // 2, y + size // 3)
        ]
        pygame.draw.polygon(screen, (100, 255, 100), ufo_points)
        pygame.draw.circle(screen, (150, 255, 150), (x, y - size // 3), size // 3)
    
    def draw_orbital_ring(self, screen, x, y):
        """Draw decorative orbital rings"""
        # Multiple rings
        rings = [170, 210, 250]
        for i, radius in enumerate(rings):
            # Dashed ring effect
            segments = 36
            for seg in range(segments):
                if seg % 3 != 0:  # Create dashed effect
                    angle1 = seg * (360 / segments)
                    angle2 = (seg + 1) * (360 / segments)
                    
                    x1 = x + int(math.cos(math.radians(angle1)) * radius)
                    y1 = y + int(math.sin(math.radians(angle1)) * radius)
                    x2 = x + int(math.cos(math.radians(angle2)) * radius)
                    y2 = y + int(math.sin(math.radians(angle2)) * radius)
                    
                    alpha = 100 - i * 20
                    color = (100, 200, 255, alpha)
                    pygame.draw.line(screen, (100, 200, 255), (x1, y1), (x2, y2), 1)
    
    def draw_title(self, screen):
        """Draw game title with effects"""
        # Pulsing glow
        pulse_size = int(10 * self.title_pulse)
        
        # Title text
        title_text = "SPACE RUN"
        title_surface = self.font_title.render(title_text, True, WHITE)
        
        # Shadow/glow layers
        for i in range(3, 0, -1):
            glow_color = (100, 200, 255, 100 - i * 20)
            glow_surface = self.font_title.render(title_text, True, (100, 200, 255))
            glow_rect = glow_surface.get_rect(center=(SCREEN_WIDTH // 2, 80 + i * 2))
            screen.blit(glow_surface, glow_rect)
        
        # Main title
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 80))
        screen.blit(title_surface, title_rect)
        
        # Subtitle
        subtitle = "Character Development Edition"
        subtitle_surface = self.font_small.render(subtitle, True, CYAN)
        subtitle_rect = subtitle_surface.get_rect(center=(SCREEN_WIDTH // 2, 130))
        screen.blit(subtitle_surface, subtitle_rect)
    
    def draw_menu_options(self, screen, high_score, character_level):
        """Draw menu buttons and info"""
        center_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT - 280
        
        # Start button (pulsing)
        start_text = "PRESS SPACE TO START"
        pulse_alpha = int(200 + 55 * self.start_button_pulse)
        start_surface = self.font_medium.render(start_text, True, (255, 255, 100))
        start_surface.set_alpha(pulse_alpha)
        start_rect = start_surface.get_rect(center=(center_x, start_y))
        
        # Button background
        button_bg = pygame.Rect(start_rect.x - 20, start_rect.y - 15, 
                               start_rect.width + 40, start_rect.height + 30)
        pygame.draw.rect(screen, (50, 100, 150, 150), button_bg, border_radius=15)
        pygame.draw.rect(screen, (100, 200, 255), button_bg, 3, border_radius=15)
        
        screen.blit(start_surface, start_rect)
        self.buttons["start"] = button_bg
        
        # Upgrade button
        upgrade_y = start_y + 70
        upgrade_text = "Press U for Upgrades"
        upgrade_surface = self.font_small.render(upgrade_text, True, WHITE)
        upgrade_rect = upgrade_surface.get_rect(center=(center_x, upgrade_y))
        screen.blit(upgrade_surface, upgrade_rect)
        
        # Character info
        info_y = upgrade_y + 60
        level_text = f"Character Level {character_level}"
        level_surface = self.font_medium.render(level_text, True, YELLOW)
        level_rect = level_surface.get_rect(center=(center_x, info_y))
        screen.blit(level_surface, level_rect)
        
        # High score
        hs_y = info_y + 45
        hs_text = f"High Score: {high_score}"
        hs_surface = self.font_small.render(hs_text, True, (200, 200, 200))
        hs_rect = hs_surface.get_rect(center=(center_x, hs_y))
        screen.blit(hs_surface, hs_rect)
    
    def draw_corner_decorations(self, screen):
        """Draw decorative elements in corners"""
        # Top left - rotating geometric shape
        self.draw_rotating_shape(screen, 80, 200, 30, 6, self.time * 50)
        
        # Top right - rotating geometric shape
        self.draw_rotating_shape(screen, SCREEN_WIDTH - 80, 200, 30, 8, -self.time * 70)
        
        # Bottom left - small planet
        self.draw_decorative_planet(screen, 100, SCREEN_HEIGHT - 100, 35, (255, 150, 200))
        
        # Bottom right - small planet
        self.draw_decorative_planet(screen, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, 35, (150, 200, 255))
    
    def draw_rotating_shape(self, screen, x, y, size, sides, rotation):
        """Draw rotating geometric shape"""
        points = []
        for i in range(sides):
            angle = math.radians(rotation + i * (360 / sides))
            px = x + int(math.cos(angle) * size)
            py = y + int(math.sin(angle) * size)
            points.append((px, py))
        
        pygame.draw.polygon(screen, (100, 200, 255), points, 2)
        
        # Inner shape
        inner_points = []
        for i in range(sides):
            angle = math.radians(rotation + i * (360 / sides))
            px = x + int(math.cos(angle) * size * 0.5)
            py = y + int(math.sin(angle) * size * 0.5)
            inner_points.append((px, py))
        
        pygame.draw.polygon(screen, (150, 230, 255), inner_points, 1)
    
    def draw_decorative_planet(self, screen, x, y, size, color):
        """Draw decorative planet in corner"""
        # Planet
        pygame.draw.circle(screen, color, (x, y), size)
        
        # Highlight
        pygame.draw.circle(screen, (255, 255, 255, 150), 
                         (x - size // 3, y - size // 3), size // 3)
        
        # Ring
        ring_rect = pygame.Rect(x - size * 1.5, y - size // 4, size * 3, size * 0.5)
        pygame.draw.ellipse(screen, (*color, 100), ring_rect, 2)
    
    def handle_click(self, pos):
        """Handle mouse clicks on buttons"""
        if "start" in self.buttons and self.buttons["start"].collidepoint(pos):
            return "start"
        return None
