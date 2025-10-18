"""
Advanced Sprite Generator - Creates animated character sprites
Uses PIL for advanced graphics and animations
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import random
import os

class AdvancedSpriteGenerator:
    """Generate high-quality animated sprites for chibi character"""
    
    def __init__(self):
        self.base_size = 160  # Larger for detail
        
    def create_advanced_chibi(self, pose="idle", frame=0):
        """Create advanced chibi character with detailed features"""
        img = Image.new('RGBA', (self.base_size, self.base_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Center coordinates
        cx, cy = self.base_size // 2, self.base_size // 2
        
        # Animation offsets based on pose
        if pose == "run":
            # Bobbing motion
            bob = math.sin(frame * 0.5) * 5
            cy += int(bob)
            leg_angle = frame * 20 % 360
        elif pose == "jump":
            # Jump arc
            cy -= 15
            leg_angle = -30
        elif pose == "boost":
            # Forward lean
            cy += 5
            leg_angle = frame * 30 % 360
        else:  # idle
            # Slight breathing motion
            bob = math.sin(frame * 0.2) * 2
            cy += int(bob)
            leg_angle = 0
        
        # Draw character components
        self.draw_body(draw, cx, cy, pose, frame)
        self.draw_head(draw, cx, cy - 30, pose, frame)
        self.draw_arms(draw, cx, cy, pose, frame)
        self.draw_legs(draw, cx, cy + 20, leg_angle, frame)
        
        return img
    
    def draw_head(self, draw, x, y, pose, frame):
        """Draw detailed chibi head with expressions"""
        head_size = 35
        
        # Head (peach skin tone)
        skin_color = (255, 220, 177)
        draw.ellipse([x-head_size, y-head_size, x+head_size, y+head_size], 
                    fill=skin_color, outline=(200, 180, 150), width=2)
        
        # Curly hair (volumous, detailed)
        hair_color = (70, 45, 25)
        # Multiple curls on top
        for i in range(8):
            angle = i * 45
            offset_x = int(math.cos(math.radians(angle)) * 30)
            offset_y = int(math.sin(math.radians(angle)) * 25) - 10
            curl_size = 15
            draw.ellipse([x+offset_x-curl_size, y+offset_y-curl_size,
                         x+offset_x+curl_size, y+offset_y+curl_size],
                        fill=hair_color, outline=(50, 30, 15), width=1)
        
        # Side fade
        for i in range(3):
            draw.ellipse([x-35-i*3, y-10+i*8, x-20-i*3, y+5+i*8],
                        fill=(60, 40, 20), outline=(40, 25, 12))
        
        # Ear
        draw.ellipse([x-35, y-5, x-25, y+5], fill=(235, 200, 160))
        draw.ellipse([x-33, y-3, x-27, y+3], fill=(220, 170, 130))
        
        # Eyes (larger, more expressive)
        eye_y = y - 5
        
        # Expression based on pose
        if pose == "boost":
            # Determined look
            eye_size = (12, 14)
        elif pose == "jump":
            # Excited look
            eye_size = (14, 16)
        else:
            # Normal look
            eye_size = (13, 15)
        
        # Right eye (visible)
        draw.ellipse([x-8, eye_y-eye_size[1]//2, x+5, eye_y+eye_size[1]//2],
                    fill=(255, 255, 255), outline=(150, 150, 150), width=1)
        # Iris
        iris_x = x - 2
        if pose == "run":
            iris_x += int(math.sin(frame * 0.3) * 2)  # Eye movement
        draw.ellipse([iris_x-5, eye_y-5, iris_x+3, eye_y+5],
                    fill=(101, 67, 33))
        # Pupil
        draw.ellipse([iris_x-3, eye_y-3, iris_x+1, eye_y+3],
                    fill=(30, 20, 10))
        # Highlight
        draw.ellipse([iris_x-2, eye_y-4, iris_x, eye_y-2],
                    fill=(255, 255, 255))
        
        # Eyebrow
        eyebrow_y = y - 15
        draw.arc([x-12, eyebrow_y-5, x+8, eyebrow_y+3],
                start=0, end=180, fill=(80, 50, 20), width=2)
        
        # Beard (subtle, detailed)
        beard_color = (90, 60, 30)
        for i in range(5):
            bx = x - 8 + i * 3
            by = y + 12 + (i % 2) * 2
            draw.ellipse([bx-2, by-2, bx+2, by+2], fill=beard_color)
        
        # Mouth (expression)
        if pose == "boost":
            # Determined smile
            draw.arc([x-8, y+5, x+8, y+15], start=0, end=180,
                    fill=(180, 100, 100), width=2)
        else:
            # Slight smile
            draw.arc([x-6, y+6, x+6, y+12], start=0, end=180,
                    fill=(200, 120, 120), width=1)
    
    def draw_body(self, draw, x, y, pose, frame):
        """Draw body with striped shirt"""
        body_width = 30
        body_height = 36  # Must be even for proper division
        
        # Tilt based on pose
        if pose == "boost":
            x += 3  # Lean forward
        
        # Body rectangle
        y = int(y)
        x = int(x)
        body_rect = [x-body_width, y-body_height//2,
                    x+body_width, y+body_height//2]
        
        # Striped pattern
        stripe_colors = [(70, 130, 180), (245, 222, 179)]
        stripe_height = 7
        for i in range(6):
            color = stripe_colors[i % 2]
            stripe_y1 = int(body_rect[1] + i * stripe_height)
            stripe_y2 = int(min(stripe_y1 + stripe_height, body_rect[3]))
            if stripe_y2 > stripe_y1:  # Only draw if valid
                draw.rectangle([int(body_rect[0]), stripe_y1, int(body_rect[2]), stripe_y2],
                             fill=color, outline=color)
        
        # Body outline
        draw.rectangle(body_rect, outline=(50, 50, 50), width=2)
    
    def draw_arms(self, draw, x, y, pose, frame):
        """Draw arms with animation"""
        arm_color = (222, 184, 135)
        
        if pose == "run":
            # Swinging arms
            left_arm_angle = math.sin(frame * 0.4) * 30
            right_arm_angle = -left_arm_angle
        elif pose == "jump":
            # Arms up
            left_arm_angle = -45
            right_arm_angle = -45
        elif pose == "boost":
            # Arms forward (driving)
            left_arm_angle = 20
            right_arm_angle = 20
        else:
            # Idle - slight movement
            left_arm_angle = math.sin(frame * 0.1) * 10
            right_arm_angle = -left_arm_angle
        
        # Left arm
        arm_length = 20
        left_x = x - 25 + int(math.cos(math.radians(left_arm_angle)) * arm_length)
        left_y = y + int(math.sin(math.radians(left_arm_angle)) * arm_length)
        draw.line([x-25, y, left_x, left_y], fill=arm_color, width=8)
        draw.ellipse([left_x-6, left_y-6, left_x+6, left_y+6], fill=arm_color)
        
        # Right arm
        right_x = x + 25 + int(math.cos(math.radians(right_arm_angle)) * arm_length)
        right_y = y + int(math.sin(math.radians(right_arm_angle)) * arm_length)
        draw.line([x+25, y, right_x, right_y], fill=arm_color, width=8)
        draw.ellipse([right_x-6, right_y-6, right_x+6, right_y+6], fill=arm_color)
    
    def draw_legs(self, draw, x, y, angle, frame):
        """Draw legs with walking animation"""
        leg_color = (60, 90, 140)  # Pants color
        shoe_color = (40, 40, 40)
        
        leg_length = 25
        
        # Left leg
        left_angle = angle
        left_x = x - 12 + int(math.cos(math.radians(left_angle)) * leg_length)
        left_y = y + int(math.sin(math.radians(left_angle)) * leg_length)
        draw.line([x-12, y, left_x, left_y], fill=leg_color, width=10)
        draw.ellipse([left_x-5, left_y-3, left_x+5, left_y+5], fill=shoe_color)
        
        # Right leg
        right_angle = angle + 180
        right_x = x + 12 + int(math.cos(math.radians(right_angle)) * leg_length)
        right_y = y + int(math.sin(math.radians(right_angle)) * leg_length)
        draw.line([x+12, y, right_x, right_y], fill=leg_color, width=10)
        draw.ellipse([right_x-5, right_y-3, right_x+5, right_y+5], fill=shoe_color)
    
    def create_hover_car_advanced(self, frame=0):
        """Create advanced hover-car with animations"""
        width, height = 200, 100
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        cx, cy = width // 2, height // 2
        
        # Hover animation
        hover_offset = int(math.sin(frame * 0.3) * 3)
        cy += hover_offset
        
        # Car body (sleek design)
        body_color = (100, 200, 220)
        shadow_color = (60, 150, 190)
        highlight_color = (150, 230, 255)
        
        # Main body shape
        body_points = [
            (20, cy),
            (width//3, cy-25),
            (width*2//3, cy-25),
            (width-20, cy),
            (width-25, cy+20),
            (25, cy+20)
        ]
        draw.polygon(body_points, fill=body_color, outline=(40, 60, 100))
        
        # Cockpit window (glossy effect)
        window_x = width // 2 - 35
        window_y = cy - 18
        draw.ellipse([window_x, window_y, window_x+70, window_y+30],
                    fill=(20, 30, 60, 200), outline=(100, 150, 200))
        # Window reflection
        draw.ellipse([window_x+5, window_y+3, window_x+30, window_y+15],
                    fill=(150, 200, 255, 100))
        
        # Solar panels with detail
        panel_color = (50, 100, 180)
        # Left panel
        panel_points_left = [
            (25, cy-30), (width//3, cy-35),
            (width//3, cy-25), (30, cy-25)
        ]
        draw.polygon(panel_points_left, fill=panel_color, outline=(30, 70, 140))
        # Panel grid
        for i in range(3):
            draw.line([30+i*15, cy-30, 30+i*15, cy-25],
                     fill=(80, 140, 220), width=1)
        
        # Right panel
        panel_points_right = [
            (width*2//3, cy-35), (width-25, cy-30),
            (width-30, cy-25), (width*2//3, cy-25)
        ]
        draw.polygon(panel_points_right, fill=panel_color, outline=(30, 70, 140))
        for i in range(3):
            draw.line([width-80+i*15, cy-35, width-80+i*15, cy-25],
                     fill=(80, 140, 220), width=1)
        
        # Engine details
        draw.rectangle([15, cy+5, 30, cy+18], fill=(30, 40, 70))
        
        # Thruster glow (animated)
        glow_intensity = int(150 + math.sin(frame * 0.5) * 100)
        for i in range(3):
            glow_size = 20 + i * 10
            alpha = max(0, glow_intensity - i * 50)
            glow_img = Image.new('RGBA', (glow_size, 15), (0, 0, 0, 0))
            glow_draw = ImageDraw.Draw(glow_img)
            glow_draw.ellipse([0, 0, glow_size, 15],
                            fill=(100, 220, 255, alpha))
            img.paste(glow_img, (5 - i*8, cy+7), glow_img)
        
        # Accent line
        draw.line([width//3, cy+5, width*2//3, cy+5],
                 fill=highlight_color, width=3)
        
        # Detail lights
        draw.ellipse([width-30, cy+3, width-24, cy+9],
                    fill=(255, 200, 50))
        
        return img
    
    def create_advanced_wheel(self, frame=0):
        """Create animated futuristic wheel"""
        size = 60
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        cx, cy = size // 2, size // 2
        
        # Outer rim
        rim_color = (60, 70, 130)
        draw.ellipse([2, 2, size-2, size-2], fill=rim_color, outline=(40, 50, 100))
        
        # Rotating inner design
        rotation = frame * 15 % 360
        for i in range(6):
            angle = rotation + i * 60
            x1 = cx + int(math.cos(math.radians(angle)) * 10)
            y1 = cy + int(math.sin(math.radians(angle)) * 10)
            x2 = cx + int(math.cos(math.radians(angle)) * 25)
            y2 = cy + int(math.sin(math.radians(angle)) * 25)
            draw.line([x1, y1, x2, y2], fill=(100, 200, 255), width=3)
        
        # Center hub
        draw.ellipse([cx-12, cy-12, cx+12, cy+12], fill=(40, 50, 90))
        
        # Glowing center (pulsing)
        glow_size = int(8 + math.sin(frame * 0.4) * 3)
        draw.ellipse([cx-glow_size, cy-glow_size, cx+glow_size, cy+glow_size],
                    fill=(150, 230, 255))
        
        # Cyan accent ring
        draw.ellipse([5, 5, size-5, size-5], outline=(100, 200, 255), width=4)
        
        return img
    
    def combine_character_and_car(self, character_pose="idle", frame=0):
        """Combine character with hover-car"""
        width, height = 220, 140
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        
        # Create components
        car = self.create_hover_car_advanced(frame)
        character = self.create_advanced_chibi(character_pose, frame)
        wheel_left = self.create_advanced_wheel(frame)
        wheel_right = self.create_advanced_wheel(frame)
        
        # Position car
        img.paste(car, (10, height - 105), car)
        
        # Position wheels
        img.paste(wheel_left, (28, height - 65), wheel_left)
        img.paste(wheel_right, (132, height - 65), wheel_right)
        
        # Position character (sitting in car)
        character_resized = character.resize((70, 100))
        img.paste(character_resized, (75, height - 115), character_resized)
        
        return img
    
    def generate_animation_sequence(self, pose="idle", frames=8):
        """Generate sequence of frames for animation"""
        sequence = []
        for i in range(frames):
            frame = self.combine_character_and_car(pose, i)
            sequence.append(frame)
        return sequence
    
    def save_sprite_sheet(self, pose="idle", frames=8):
        """Save all frames as sprite sheet"""
        sequence = self.generate_animation_sequence(pose, frames)
        
        # Create sprite sheet
        frame_width = sequence[0].width
        frame_height = sequence[0].height
        sheet_width = frame_width * frames
        sheet_height = frame_height
        
        sprite_sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))
        
        for i, frame in enumerate(sequence):
            sprite_sheet.paste(frame, (i * frame_width, 0), frame)
        
        return sprite_sheet
    
    def generate_all_animations(self):
        """Generate all character animations"""
        print("🎨 Generating advanced character animations...")
        
        os.makedirs("assets/images/player/animations", exist_ok=True)
        
        animations = {
            "idle": 8,
            "run": 8,
            "jump": 4,
            "boost": 8
        }
        
        for pose, frame_count in animations.items():
            print(f"  → Creating {pose} animation ({frame_count} frames)...")
            sprite_sheet = self.save_sprite_sheet(pose, frame_count)
            sprite_sheet.save(f"assets/images/player/animations/{pose}.png")
            
            # Save individual frames too
            for i in range(frame_count):
                frame = self.combine_character_and_car(pose, i)
                frame.save(f"assets/images/player/animations/{pose}_frame_{i}.png")
        
        print("✅ All animations generated!")

if __name__ == "__main__":
    generator = AdvancedSpriteGenerator()
    generator.generate_all_animations()
