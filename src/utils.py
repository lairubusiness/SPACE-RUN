"""
Utility functions and helpers
"""

import pygame

def load_image(path, scale=None):
    """Load and optionally scale an image"""
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except pygame.error as e:
        print(f"Error loading image {path}: {e}")
        return None

def load_sound(path):
    """Load a sound effect"""
    try:
        sound = pygame.mixer.Sound(path)
        return sound
    except pygame.error as e:
        print(f"Error loading sound {path}: {e}")
        return None

def clamp(value, min_value, max_value):
    """Clamp a value between min and max"""
    return max(min_value, min(value, max_value))

def lerp(start, end, t):
    """Linear interpolation between start and end"""
    return start + (end - start) * t

def distance(point1, point2):
    """Calculate distance between two points"""
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return (dx * dx + dy * dy) ** 0.5

def draw_text_centered(screen, font, text, color, center_pos):
    """Draw text centered at position"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center_pos)
    screen.blit(text_surface, text_rect)
    return text_rect

def create_gradient_surface(width, height, color1, color2, vertical=True):
    """Create a surface with a gradient"""
    surface = pygame.Surface((width, height))
    
    if vertical:
        for y in range(height):
            ratio = y / height
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            pygame.draw.line(surface, (r, g, b), (0, y), (width, y))
    else:
        for x in range(width):
            ratio = x / width
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            pygame.draw.line(surface, (r, g, b), (x, 0), (x, height))
    
    return surface
