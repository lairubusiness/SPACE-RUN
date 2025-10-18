# 🚀 SPACE RUN

A thrilling 2D endless runner space adventure game built with Python and Pygame!

## 🎮 Game Overview

**Title:** SPACE RUN  
**Genre:** 2D Endless Runner  
**Theme:** Space Adventure with colorful planets, asteroids, and UFOs  

Drive your futuristic hover-car through the depths of space, avoiding obstacles and collecting energy orbs. How far can you go?

## ✨ Features

- 🎯 **Endless Runner Gameplay** - Procedurally generated obstacles
- 🚗 **Chibi Character** - Cute driver in a futuristic hover-car
- 🌌 **Parallax Scrolling** - Beautiful layered space backgrounds
- ⚡ **Power-ups** - Energy orbs, shields, and speed boosts
- 🎵 **Sound Effects** - Immersive audio experience
- 💾 **Save System** - Persistent high scores and player progression
- 🎨 **Dynamic Difficulty** - Speed increases as you progress
- 🏆 **Upgrade System** - Improve your abilities over time

## 🎯 Game Mechanics

### Controls
- **SPACE** - Jump
- **SHIFT** - Activate Boost
- **ESC** - Pause/Menu

### Objectives
1. **Survive** as long as possible
2. **Collect** energy orbs for points
3. **Avoid** asteroids and UFOs
4. **Use** power-ups strategically

### Obstacles
- **Asteroids** - Rotating space rocks at varying speeds
- **UFOs** - Flying enemies with wave patterns

### Power-ups
- **Energy Orbs** - Increase your score
- **Shields** - Protect from one hit

## 📁 Project Structure

```
SPACE_GAME/
│
├── main.py                     # Game entry point
│
├── assets/
│   ├── images/
│   │   ├── player/            # Player sprites
│   │   ├── enemies/           # Enemy sprites
│   │   ├── backgrounds/       # Background layers
│   │   └── ui/                # UI elements
│   ├── sounds/                # Sound effects and music
│   └── fonts/                 # Custom fonts
│
├── src/
│   ├── __init__.py
│   ├── settings.py            # Game configuration
│   ├── game.py                # Core game loop
│   ├── player.py              # Player logic
│   ├── enemy.py               # Enemy management
│   ├── background.py          # Parallax scrolling
│   ├── ui.py                  # Menus and HUD
│   ├── powerups.py            # Power-up system
│   ├── save_load.py           # Save/load functionality
│   └── utils.py               # Helper functions
│
├── data/
│   └── save_data.json         # Player progression data
│
└── README.md                  # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install pygame
```

Or use the requirements file (create one):

```bash
pip install -r requirements.txt
```

### Step 2: Run the Game

```bash
python main.py
```

## 🎨 Adding Custom Assets

### Images
Place your custom sprites in the appropriate folders:
- **Player sprites:** `assets/images/player/`
- **Enemy sprites:** `assets/images/enemies/`
- **Backgrounds:** `assets/images/backgrounds/`
- **UI elements:** `assets/images/ui/`

Recommended image formats: PNG with transparency

### Sounds
Add sound files to `assets/sounds/`:
- Background music (MP3)
- Sound effects (WAV)

### Fonts
Place custom TrueType fonts (.ttf) in `assets/fonts/`

## 🛠️ Development

### Game Settings
Edit `src/settings.py` to customize:
- Screen resolution
- Game speed and difficulty
- Player physics
- Spawn rates
- Colors and UI settings

### Adding New Features
The modular structure makes it easy to extend:
1. **New enemies** - Add classes in `src/enemy.py`
2. **New power-ups** - Extend `src/powerups.py`
3. **New game modes** - Modify `src/game.py`

## 🎮 Game States

1. **MENU** - Main menu with high score display
2. **PLAYING** - Active gameplay
3. **PAUSED** - Game paused
4. **GAME_OVER** - End screen with score summary

## 💾 Save System

Player data is automatically saved to `data/save_data.json`:
- High score
- Player level
- Experience points
- Upgrade levels

## 🐛 Troubleshooting

### Game won't start
- Ensure Pygame is installed: `pip install pygame`
- Check Python version: `python --version`

### No sound
- Verify sound files are in `assets/sounds/`
- Check system audio settings

### Performance issues
- Reduce screen resolution in `src/settings.py`
- Lower FPS setting if needed

## 📝 TODO / Future Features

- [ ] Add more enemy types
- [ ] Implement boss battles
- [ ] Add multiplayer mode
- [ ] Create level system
- [ ] Add achievements
- [ ] Implement particle effects
- [ ] Add mobile controls
- [ ] Create tutorial mode

## 🤝 Contributing

This is a personal project, but suggestions are welcome!

## 📜 License

This project is for educational and personal use.

## 🎯 Credits

**Developer:** Your Name  
**Engine:** Pygame  
**Art Style:** Chibi/Cute  
**Theme:** Space Adventure  

## 📞 Support

For issues or questions, please refer to the Pygame documentation:
- [Pygame Docs](https://www.pygame.org/docs/)
- [Python Docs](https://docs.python.org/)

---

**Enjoy your space adventure! 🚀✨**

*Remember: The sky is not the limit when you're in space!*
