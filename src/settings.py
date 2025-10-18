"""
Global game settings and constants
"""

# Screen settings
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
FPS = 60
GAME_TITLE = "SPACE RUN"
GROUND_LEVEL = 420

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
PURPLE = (200, 0, 255)
CYAN = (0, 255, 255)

# Game settings
GRAVITY = 1500  # Pixels per second squared
GROUND_HEIGHT = 150  # Height of ground from bottom
SCROLL_SPEED = 300  # Initial background scroll speed (pixels/second)
MAX_SCROLL_SPEED = 800  # Maximum scroll speed
SPEED_INCREASE_RATE = 10  # Speed increase per second

# Player settings
PLAYER_START_X = 200
PLAYER_START_Y = SCREEN_HEIGHT - GROUND_HEIGHT - 100
PLAYER_JUMP_VELOCITY = -600  # Negative for upward jump
PLAYER_BOOST_DURATION = 2.0  # Seconds
PLAYER_SIZE = (80, 80)

# Enemy settings
ENEMY_SPAWN_RATE = 2.0  # Seconds between spawns
ENEMY_MIN_GAP = 200  # Minimum gap between enemies
ASTEROID_SPEED_MIN = 250
ASTEROID_SPEED_MAX = 400
UFO_SPEED = 350

# Powerup settings
POWERUP_SPAWN_RATE = 5.0  # Seconds
ORB_SCORE = 10
SHIELD_DURATION = 5.0  # Seconds

# UI settings
FONT_SIZE_LARGE = 48
FONT_SIZE_MEDIUM = 32
FONT_SIZE_SMALL = 24
HUD_MARGIN = 20

# File paths
SAVE_FILE = "data/save_data.json"
