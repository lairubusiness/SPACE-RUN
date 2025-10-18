"""
UI elements: menus, HUD, buttons, score display
"""

import pygame
from src.settings import *

class UI:
    """Handles all UI rendering"""
    
    def __init__(self):
        # Initialize fonts
        pygame.font.init()
        self.font_large = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(None, FONT_SIZE_SMALL)
    
    def draw_text(self, screen, text, font, color, x, y, center=False):
        """Helper method to draw text"""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)
    
    def draw_menu(self, screen, high_score):
        """Draw main menu"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        self.draw_text(screen, "SPACE RUN", self.font_large, CYAN, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, center=True)
        self.draw_text(screen, "Press SPACE to Start", self.font_medium, WHITE, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, center=True)
        self.draw_text(screen, "Controls: SPACE = Jump | SHIFT = Boost", self.font_small, WHITE, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, center=True)
        self.draw_text(screen, f"High Score: {high_score}", self.font_medium, YELLOW, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120, center=True)
    
    def draw_hud(self, screen, score, distance, player):
        """Draw heads-up display during gameplay"""
        self.draw_text(screen, f"Score: {score}", self.font_medium, WHITE, HUD_MARGIN, HUD_MARGIN)
        self.draw_text(screen, f"Distance: {distance}m", self.font_medium, WHITE, HUD_MARGIN, HUD_MARGIN + 40)
        
        if player.boost_active:
            boost_text = f"BOOST: {player.boost_timer:.1f}s"
            self.draw_text(screen, boost_text, self.font_small, YELLOW, HUD_MARGIN, HUD_MARGIN + 80)
        
        if player.has_shield:
            shield_text = f"SHIELD: {player.shield_timer:.1f}s"
            self.draw_text(screen, shield_text, self.font_small, CYAN, HUD_MARGIN, HUD_MARGIN + 110)
    
    def draw_pause(self, screen):
        """Draw pause overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        self.draw_text(screen, "PAUSED", self.font_large, WHITE, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, center=True)
        self.draw_text(screen, "Press ESC to Resume | Q to Quit", self.font_medium, WHITE, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, center=True)
    
    def draw_game_over(self, screen, score, high_score):
        """Draw game over screen"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        self.draw_text(screen, "GAME OVER", self.font_large, RED, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, center=True)
        self.draw_text(screen, f"Score: {score}", self.font_medium, WHITE, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, center=True)
        self.draw_text(screen, f"High Score: {high_score}", self.font_medium, YELLOW, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, center=True)
        self.draw_text(screen, "Press SPACE to Restart | ESC for Menu", self.font_small, WHITE, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, center=True)
