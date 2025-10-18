"""Helper script to switch between simple and advanced game modes"""
import os
import shutil

# Backup current game.py as game_advanced.py
if os.path.exists("src/game.py"):
    shutil.copy("src/game.py", "src/game_advanced.py")
    print("✓ Backed up advanced game.py")

# Replace with simple version
if os.path.exists("src/game_simple.py"):
    shutil.copy("src/game_simple.py", "src/game.py")
    print("✓ Using simplified game.py")
else:
    print("✗ game_simple.py not found")

print("\n✅ Game files updated! The game now uses the simplified structure.")
print("   Advanced version saved as: src/game_advanced.py")
