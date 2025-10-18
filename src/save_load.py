"""
Save and load player progression data
"""

import json
import os
from src.settings import SAVE_FILE

class SaveManager:
    """Handles saving and loading game data"""
    
    def __init__(self):
        self.save_path = SAVE_FILE
        self.ensure_save_directory()
    
    def ensure_save_directory(self):
        """Create save directory if it doesn't exist"""
        directory = os.path.dirname(self.save_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
    
    def save(self, data):
        """Save game data to JSON file"""
        try:
            with open(self.save_path, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving game data: {e}")
            return False
    
    def load(self):
        """Load game data from JSON file"""
        if not os.path.exists(self.save_path):
            return self.get_default_data()
        
        try:
            with open(self.save_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error loading game data: {e}")
            return self.get_default_data()
    
    def get_default_data(self):
        """Get default save data structure"""
        return {
            "high_score": 0,
            "player_stats": {
                "level": 1,
                "experience": 0,
                "upgrades": {
                    "jump_power": 0,
                    "boost_duration": 0,
                    "shield_duration": 0
                }
            }
        }
    
    def delete_save(self):
        """Delete save file"""
        if os.path.exists(self.save_path):
            try:
                os.remove(self.save_path)
                return True
            except Exception as e:
                print(f"Error deleting save file: {e}")
                return False
        return True
