"""
SPACE RUN - Advanced Character Development Edition
Launch the game with full RPG progression system
"""

from src.game_with_development import AdvancedGame

if __name__ == "__main__":
    print("🚀 Starting SPACE RUN - Character Development Edition")
    print("=" * 50)
    print("Features:")
    print("  ✓ Animated Character Sprites")
    print("  ✓ RPG-Style Leveling System")
    print("  ✓ Skill Tree with 6 Upgrades")
    print("  ✓ Unlockable Abilities")
    print("  ✓ Energy System")
    print("  ✓ Advanced Particle Effects")
    print("  ✓ Character Progression Saving")
    print("=" * 50)
    print("\nControls:")
    print("  SPACE - Jump")
    print("  SHIFT - Boost (uses energy)")
    print("  U - Open Upgrade Screen")
    print("  ESC - Pause/Menu")
    print("\nStarting game...")
    
    game = AdvancedGame()
    game.run()
