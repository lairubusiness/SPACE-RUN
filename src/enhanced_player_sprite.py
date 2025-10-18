"""
Enhanced Player Sprite - Uses actual character image
Combines your chibi character with the hover car
"""

import pygame
from PIL import Image

def create_player_with_real_character():
    """Create player sprite using the actual character image"""
    try:
        # Load the character face image
        character_img = Image.open("C:/Users/LENOVO/Downloads/SPACE_GAME/IMAGE/Gemini_Generated_Image_o7cv55o7cv55o7cv.png")
        
        # Load the hover car
        try:
            car_img = Image.open("assets/images/player/car.png")
        except:
            # Create a simple car if not found
            car_img = create_simple_car()
        
        # Create combined sprite
        width, height = 160, 120
        combined = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        
        # Resize and position car (bottom portion)
        car_resized = car_img.resize((140, 70))
        combined.paste(car_resized, (10, height - 75), car_resized)
        
        # Resize and position character (top portion, sitting in car)
        char_resized = character_img.resize((70, 80))
        combined.paste(char_resized, (45, height - 100), char_resized)
        
        # Save the combined sprite
        combined.save("assets/images/player/player_with_real_character.png")
        
        # Convert to pygame surface
        pygame_img = pygame.image.load("assets/images/player/player_with_real_character.png").convert_alpha()
        
        return pygame_img
        
    except Exception as e:
        print(f"Error creating player sprite with real character: {e}")
        return None

def create_simple_car():
    """Create a simple car placeholder"""
    from PIL import ImageDraw
    
    car = Image.new('RGBA', (140, 70), (0, 0, 0, 0))
    draw = ImageDraw.Draw(car)
    
    # Car body (cyan)
    body_color = (100, 200, 220)
    draw.rectangle([10, 20, 130, 60], fill=body_color, outline=(60, 150, 190), width=2)
    
    # Cockpit
    draw.rectangle([50, 10, 90, 35], fill=(20, 30, 60))
    
    # Wheels
    wheel_color = (60, 70, 130)
    draw.ellipse([25, 50, 45, 70], fill=wheel_color, outline=(100, 200, 255), width=2)
    draw.ellipse([95, 50, 115, 70], fill=wheel_color, outline=(100, 200, 255), width=2)
    
    return car

def generate_sprite_file():
    """Generate and save the sprite without pygame"""
    import os
    from PIL import Image, ImageDraw
    
    os.makedirs("assets/images/player", exist_ok=True)
    
    try:
        # Load the character face image
        character_img = Image.open("C:/Users/LENOVO/Downloads/SPACE_GAME/IMAGE/Gemini_Generated_Image_o7cv55o7cv55o7cv.png")
        
        # Load the hover car
        try:
            car_img = Image.open("assets/images/player/car.png")
        except:
            # Create a simple car
            car_img = create_simple_car()
        
        # Create combined sprite
        width, height = 160, 120
        combined = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        
        # Resize and position car (bottom portion)
        car_resized = car_img.resize((140, 70))
        combined.paste(car_resized, (10, height - 75), car_resized)
        
        # Resize and position character (top portion, sitting in car)
        char_resized = character_img.resize((70, 80))
        combined.paste(char_resized, (45, height - 100), char_resized)
        
        # Save the combined sprite
        combined.save("assets/images/player/player_with_real_character.png")
        
        print("✅ Player sprite with real character created successfully!")
        print("   Saved to: assets/images/player/player_with_real_character.png")
        return True
        
    except Exception as e:
        print(f"❌ Error creating player sprite: {e}")
        return False

if __name__ == "__main__":
    generate_sprite_file()
