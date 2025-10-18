"""
Advanced Asset Generator - Creates all game graphics using Python
Generates chibi character, hover-car, backgrounds, enemies, power-ups
"""

import pygame
import math
import random
from src.settings import *

class AssetGenerator:
    """Advanced procedural asset generation for Space Run"""
    
    def __init__(self):
        """Initialize the asset generator"""
        pygame.init()
        
    # ============ PLAYER ASSETS ============
    
    def create_chibi_character(self, size=80):
        """Create chibi character with curly hair and beard"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Body/Shirt (striped pattern)
        body_rect = pygame.Rect(size//4, size//2, size//2, size//3)
        for i in range(5):
            stripe_color = (70, 130, 180) if i % 2 == 0 else (245, 222, 179)
            pygame.draw.rect(surface, stripe_color, 
                           (body_rect.x, body_rect.y + i * 6, body_rect.width, 6))
        
        # Arms
        arm_color = (222, 184, 135)
        pygame.draw.circle(surface, arm_color, (size//4 + 5, size//2 + 10), 8)
        pygame.draw.circle(surface, arm_color, (size*3//4 - 5, size//2 + 10), 8)
        
        # Head (peach tone)
        head_color = (255, 220, 177)
        pygame.draw.circle(surface, head_color, (size//2, size//3), size//5)
        
        # Ear
        pygame.draw.circle(surface, (235, 200, 160), (size//2 - size//6, size//3), size//12)
        pygame.draw.circle(surface, (220, 170, 130), (size//2 - size//6, size//3), size//18)
        
        # Eye (large chibi eye)
        eye_white = (255, 255, 255)
        eye_brown = (101, 67, 33)
        pygame.draw.ellipse(surface, eye_white, (size//2 - 8, size//3 - 5, 14, 16))
        pygame.draw.circle(surface, eye_brown, (size//2 - 2, size//3), 5)
        pygame.draw.circle(surface, (255, 255, 255), (size//2 - 1, size//3 - 2), 2)
        
        # Eyebrow
        pygame.draw.arc(surface, (80, 50, 20), (size//2 - 10, size//3 - 12, 16, 8), 
                       0, math.pi, 2)
        
        # Beard (subtle)
        beard_color = (90, 60, 30)
        for i in range(3):
            pygame.draw.circle(surface, beard_color, 
                             (size//2 - 5 + i*3, size//3 + 10), 2)
        
        # Curly hair (volumous)
        hair_color = (70, 45, 25)
        # Top curls
        for i in range(6):
            angle = i * 30
            x = size//2 + int(math.cos(math.radians(angle)) * size//5)
            y = size//3 - size//6 + int(math.sin(math.radians(angle)) * size//8)
            pygame.draw.circle(surface, hair_color, (x, y), size//8)
        
        # Side fade
        for i in range(3):
            pygame.draw.circle(surface, (60, 40, 20), 
                             (size//2 - size//5, size//3 - 5 + i*5), size//10)
        
        return surface
    
    def create_hover_car(self, width=120, height=60):
        """Create futuristic cyan hover-car with solar panels"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Main body (cyan/blue gradient)
        body_colors = [(100, 200, 220), (70, 170, 200), (60, 150, 190)]
        
        # Car body shape
        body_points = [
            (10, height//2),
            (width//4, height//3),
            (width*3//4, height//3),
            (width - 10, height//2),
            (width - 15, height*2//3),
            (15, height*2//3)
        ]
        pygame.draw.polygon(surface, body_colors[1], body_points)
        
        # Dark outline
        pygame.draw.polygon(surface, (40, 60, 100), body_points, 3)
        
        # Cockpit window
        window_rect = pygame.Rect(width//3, height//3 + 5, width//3, height//4)
        pygame.draw.rect(surface, (20, 30, 60), window_rect, border_radius=5)
        pygame.draw.rect(surface, (100, 150, 200), window_rect.inflate(-4, -4), border_radius=4)
        
        # Solar panels on top
        panel_color = (50, 100, 180)
        panel_highlight = (80, 140, 220)
        
        # Left panel
        panel1 = [(15, height//3 - 5), (width//3, height//3 - 8), 
                  (width//3, height//3), (20, height//3)]
        pygame.draw.polygon(surface, panel_color, panel1)
        pygame.draw.line(surface, panel_highlight, panel1[0], panel1[1], 2)
        
        # Right panel
        panel2 = [(width*2//3, height//3 - 8), (width - 15, height//3 - 5),
                  (width - 20, height//3), (width*2//3, height//3)]
        pygame.draw.polygon(surface, panel_color, panel2)
        pygame.draw.line(surface, panel_highlight, panel2[0], panel2[1], 2)
        
        # Engine exhaust ports
        exhaust_color = (30, 40, 70)
        pygame.draw.rect(surface, exhaust_color, (5, height//2 + 5, 12, 8), border_radius=2)
        
        # Details/vents
        for i in range(3):
            pygame.draw.line(surface, (40, 80, 120), 
                           (width//2 + i*8, height*2//3 - 5),
                           (width//2 + i*8, height*2//3 + 5), 1)
        
        # Side accent
        pygame.draw.line(surface, (120, 220, 255), 
                        (width//4, height//2), (width*3//4, height//2), 2)
        
        # Yellow detail light
        pygame.draw.circle(surface, (255, 200, 50), (width - 25, height//2), 3)
        
        return surface
    
    def create_futuristic_wheel(self, size=40):
        """Create animated futuristic wheel"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Outer rim (dark blue/purple)
        rim_color = (60, 70, 130)
        pygame.draw.circle(surface, rim_color, (size//2, size//2), size//2)
        
        # Inner rim (cyan accent)
        pygame.draw.circle(surface, (100, 200, 255), (size//2, size//2), size//2 - 4, 3)
        
        # Center hub
        hub_color = (40, 50, 90)
        pygame.draw.circle(surface, hub_color, (size//2, size//2), size//4)
        
        # Cyan glow center
        pygame.draw.circle(surface, (150, 230, 255), (size//2, size//2), size//5)
        
        # Spokes (tech design)
        for i in range(6):
            angle = i * 60
            x1 = size//2 + int(math.cos(math.radians(angle)) * size//4)
            y1 = size//2 + int(math.sin(math.radians(angle)) * size//4)
            x2 = size//2 + int(math.cos(math.radians(angle)) * (size//2 - 4))
            y2 = size//2 + int(math.sin(math.radians(angle)) * (size//2 - 4))
            pygame.draw.line(surface, (80, 150, 200), (x1, y1), (x2, y2), 2)
        
        return surface
    
    def create_player_with_car(self, width=140, height=90):
        """Combine chibi character with hover-car"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Create components
        car = self.create_hover_car(120, 60)
        character = self.create_chibi_character(65)
        wheel_left = self.create_futuristic_wheel(35)
        wheel_right = self.create_futuristic_wheel(35)
        
        # Position car
        surface.blit(car, (10, height - 65))
        
        # Position wheels
        surface.blit(wheel_left, (22, height - 40))
        surface.blit(wheel_right, (90, height - 40))
        
        # Position character (sitting in car)
        surface.blit(character, (45, height - 85))
        
        # Thruster flame effect
        flame_color = (100, 220, 255)
        for i in range(3):
            flame_x = 8 - i * 6
            flame_alpha = 255 - i * 80
            flame = pygame.Surface((15 + i*5, 8), pygame.SRCALPHA)
            pygame.draw.ellipse(flame, (*flame_color, flame_alpha), flame.get_rect())
            surface.blit(flame, (flame_x, height - 55))
        
        return surface
    
    # ============ BACKGROUND ASSETS ============
    
    def create_space_background(self, width, height):
        """Create beautiful space background with gradient"""
        surface = pygame.Surface((width, height))
        
        # Create gradient from dark blue to purple
        for y in range(height):
            ratio = y / height
            # Deep space blue to purple gradient
            r = int(10 + (60 - 10) * ratio)
            g = int(10 + (30 - 10) * ratio)
            b = int(40 + (90 - 40) * ratio)
            pygame.draw.line(surface, (r, g, b), (0, y), (width, y))
        
        return surface
    
    def create_star_field(self, width, height, count=150):
        """Create twinkling stars"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
        for _ in range(count):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.choice([1, 1, 1, 2, 2, 3])
            brightness = random.randint(150, 255)
            color = (brightness, brightness, brightness)
            
            pygame.draw.circle(surface, color, (x, y), size)
            
            # Add cross glow to some stars
            if size >= 2 and random.random() > 0.7:
                pygame.draw.line(surface, (*color, 100), (x-3, y), (x+3, y), 1)
                pygame.draw.line(surface, (*color, 100), (x, y-3), (x, y+3), 1)
        
        return surface
    
    def create_planet(self, size, planet_type='earth'):
        """Create colorful planet"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        colors = {
            'earth': [(80, 150, 200), (100, 180, 220), (60, 120, 160)],
            'mars': [(200, 100, 80), (220, 120, 90), (180, 80, 60)],
            'purple': [(180, 100, 200), (200, 120, 220), (160, 80, 180)],
            'pink': [(255, 150, 180), (255, 180, 200), (220, 120, 150)]
        }
        
        planet_colors = colors.get(planet_type, colors['earth'])
        
        # Base planet
        pygame.draw.circle(surface, planet_colors[0], (size//2, size//2), size//2)
        
        # Add some surface details (continents/spots)
        for _ in range(random.randint(3, 6)):
            x = random.randint(size//4, size*3//4)
            y = random.randint(size//4, size*3//4)
            spot_size = random.randint(size//8, size//4)
            pygame.draw.circle(surface, planet_colors[1], (x, y), spot_size)
        
        # Highlight (makes it look spherical)
        highlight_size = size // 3
        pygame.draw.circle(surface, (*planet_colors[2], 100), 
                         (size//3, size//3), highlight_size)
        
        # Shadow side
        shadow = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(shadow, (0, 0, 0, 80), (size*2//3, size*2//3), size//2)
        surface.blit(shadow, (0, 0))
        
        return surface
    
    def create_grid_ground(self, width, height=150):
        """Create futuristic grid ground"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Grid lines
        grid_color = (80, 120, 180)
        spacing = 40
        
        # Horizontal lines with perspective
        for i in range(5):
            y = i * 30
            thickness = 2 if i == 0 else 1
            alpha = 255 - i * 40
            color = (*grid_color, alpha)
            line_surf = pygame.Surface((width, thickness), pygame.SRCALPHA)
            line_surf.fill(color)
            surface.blit(line_surf, (0, y))
        
        # Vertical lines
        for i in range(width // spacing):
            x = i * spacing
            pygame.draw.line(surface, (*grid_color, 150), (x, 0), (x, height), 1)
        
        # Circuit pattern
        for _ in range(8):
            x = random.randint(0, width)
            y = random.randint(0, height)
            pygame.draw.circle(surface, (100, 200, 255), (x, y), 3)
            pygame.draw.line(surface, (100, 200, 255), (x, y), 
                           (x + random.randint(-30, 30), y), 2)
        
        return surface
    
    # ============ ENEMY ASSETS ============
    
    def create_asteroid(self, size):
        """Create rotating asteroid"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Create irregular asteroid shape
        points = []
        num_points = random.randint(8, 12)
        for i in range(num_points):
            angle = (360 / num_points) * i
            radius = size // 2 * random.uniform(0.7, 1.0)
            x = size // 2 + radius * math.cos(math.radians(angle))
            y = size // 2 + radius * math.sin(math.radians(angle))
            points.append((x, y))
        
        # Draw asteroid
        pygame.draw.polygon(surface, (120, 80, 50), points)
        pygame.draw.polygon(surface, (80, 50, 30), points, 2)
        
        # Add craters
        for _ in range(random.randint(2, 4)):
            cx = random.randint(size//4, size*3//4)
            cy = random.randint(size//4, size*3//4)
            crater_size = random.randint(size//10, size//5)
            pygame.draw.circle(surface, (90, 60, 40), (cx, cy), crater_size)
            pygame.draw.circle(surface, (70, 45, 30), (cx, cy), crater_size, 1)
        
        return surface
    
    def create_ufo(self, width=70, height=40):
        """Create enemy UFO"""
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # UFO body (saucer shape)
        body_color = (100, 180, 100)
        dome_color = (150, 220, 150)
        
        # Bottom saucer
        ellipse_rect = pygame.Rect(5, height//2, width - 10, height//3)
        pygame.draw.ellipse(surface, body_color, ellipse_rect)
        pygame.draw.ellipse(surface, (70, 140, 70), ellipse_rect, 2)
        
        # Top dome
        dome_rect = pygame.Rect(width//4, height//6, width//2, height//2)
        pygame.draw.ellipse(surface, dome_color, dome_rect)
        
        # Windows
        for i in range(3):
            window_x = width//4 + i * width//6
            pygame.draw.circle(surface, (255, 255, 100), (window_x, height//3), 5)
            pygame.draw.circle(surface, (200, 200, 50), (window_x, height//3), 5, 1)
        
        # Lights underneath
        for i in range(4):
            light_x = width//5 + i * width//6
            pygame.draw.circle(surface, (100, 200, 255), (light_x, height*2//3), 3)
        
        return surface
    
    # ============ POWER-UP ASSETS ============
    
    def create_energy_orb(self, size=30):
        """Create glowing energy orb"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Outer glow
        for i in range(5, 0, -1):
            alpha = 50 * (6 - i)
            radius = size // 2 - i
            color = (255, 220, 50, alpha)
            glow = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.circle(glow, color, (size//2, size//2), size//2 - i + 5)
            surface.blit(glow, (0, 0))
        
        # Core
        pygame.draw.circle(surface, (255, 240, 100), (size//2, size//2), size//3)
        pygame.draw.circle(surface, (255, 255, 200), (size//2, size//2), size//5)
        
        # Sparkle
        pygame.draw.circle(surface, (255, 255, 255), (size//2 - 3, size//2 - 3), 3)
        
        return surface
    
    def create_shield_powerup(self, size=35):
        """Create shield power-up"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Shield shape (hexagon)
        points = []
        for i in range(6):
            angle = i * 60
            x = size // 2 + (size // 2 - 5) * math.cos(math.radians(angle))
            y = size // 2 + (size // 2 - 5) * math.sin(math.radians(angle))
            points.append((x, y))
        
        # Draw shield
        pygame.draw.polygon(surface, (100, 200, 255, 180), points)
        pygame.draw.polygon(surface, (150, 220, 255), points, 3)
        
        # Inner glow
        inner_points = []
        for i in range(6):
            angle = i * 60
            x = size // 2 + (size // 3) * math.cos(math.radians(angle))
            y = size // 2 + (size // 3) * math.sin(math.radians(angle))
            inner_points.append((x, y))
        pygame.draw.polygon(surface, (200, 240, 255, 100), inner_points)
        
        return surface
    
    # ============ UI ASSETS ============
    
    def create_boost_icon(self, size=30):
        """Create boost/flame icon"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Flame shape
        flame_points = [
            (size//2, 5),
            (size*3//4, size//3),
            (size*2//3, size*2//3),
            (size//2, size - 5),
            (size//3, size*2//3),
            (size//4, size//3)
        ]
        
        # Outer flame (orange)
        pygame.draw.polygon(surface, (255, 150, 50), flame_points)
        # Inner flame (yellow)
        inner_points = [(p[0], p[1] + 5) for p in flame_points]
        pygame.draw.polygon(surface, (255, 220, 100), inner_points)
        
        return surface
    
    def generate_all_assets(self):
        """Generate and save all game assets"""
        print("🎨 Generating all game assets...")
        
        # Create directories if needed
        import os
        os.makedirs("assets/images/player", exist_ok=True)
        os.makedirs("assets/images/enemies", exist_ok=True)
        os.makedirs("assets/images/backgrounds", exist_ok=True)
        os.makedirs("assets/images/powerups", exist_ok=True)
        os.makedirs("assets/images/ui", exist_ok=True)
        
        # Generate player assets
        print("  → Creating player sprites...")
        player_car = self.create_player_with_car(140, 90)
        pygame.image.save(player_car, "assets/images/player/car.png")
        
        character = self.create_chibi_character(80)
        pygame.image.save(character, "assets/images/player/idle.png")
        
        wheel = self.create_futuristic_wheel(40)
        pygame.image.save(wheel, "assets/images/player/wheel.png")
        
        # Generate backgrounds
        print("  → Creating backgrounds...")
        space_bg = self.create_space_background(1920, 720)
        pygame.image.save(space_bg, "assets/images/backgrounds/space_bg.png")
        
        stars = self.create_star_field(1920, 720, 200)
        pygame.image.save(stars, "assets/images/backgrounds/stars_layer.png")
        
        ground = self.create_grid_ground(1920, 150)
        pygame.image.save(ground, "assets/images/backgrounds/grid_ground.png")
        
        # Generate planets
        print("  → Creating planets...")
        for ptype, name in [('earth', 'planet_blue'), ('mars', 'planet_red'), 
                           ('purple', 'planet_purple'), ('pink', 'planet_pink')]:
            planet = self.create_planet(80, ptype)
            pygame.image.save(planet, f"assets/images/backgrounds/{name}.png")
        
        # Generate enemies
        print("  → Creating enemies...")
        for i, size in enumerate([50, 60, 70, 80]):
            asteroid = self.create_asteroid(size)
            pygame.image.save(asteroid, f"assets/images/enemies/asteroid_{i+1}.png")
        
        ufo = self.create_ufo(70, 40)
        pygame.image.save(ufo, "assets/images/enemies/ufo.png")
        
        # Generate power-ups
        print("  → Creating power-ups...")
        orb = self.create_energy_orb(30)
        pygame.image.save(orb, "assets/images/powerups/energy_orb.png")
        
        shield = self.create_shield_powerup(35)
        pygame.image.save(shield, "assets/images/powerups/shield.png")
        
        # Generate UI
        print("  → Creating UI elements...")
        boost = self.create_boost_icon(30)
        pygame.image.save(boost, "assets/images/ui/boost_icon.png")
        
        print("✅ All assets generated successfully!")
        print(f"   Assets saved to: assets/images/")

# Command-line usage
if __name__ == "__main__":
    generator = AssetGenerator()
    generator.generate_all_assets()
