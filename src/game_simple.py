"""
Core game loop - Simplified structure
"""

import pygame
from src.settings import *
from src.player import Player
from src.background import Background

class Game:
    """Main game class that handles game loop"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.bg = Background()
        self.running = True

    def run(self):
        """Main game loop"""
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Update game objects"""
        dt = self.clock.get_time() / 1000.0  # Delta time in seconds
        self.player.update(dt)
        self.bg.update(dt, 300)  # Use default scroll speed

    def draw(self):
        """Draw everything to screen"""
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
