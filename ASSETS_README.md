# 🎨 SPACE RUN - Asset Generation System

## Overview
All game assets are **procedurally generated using Python** (Pygame) - no external images needed! The asset generator creates beautiful, game-ready graphics that match your chibi space theme.

## 📁 Generated Assets

### Player Assets (`assets/images/player/`)
- **`car.png`** - Complete chibi character driving futuristic hover-car
  - Chibi character with curly hair and beard
  - Striped shirt (blue and beige)
  - Cyan/blue hover-car with solar panels
  - Futuristic wheels with glowing centers
  - Thruster flame effects
  
- **`idle.png`** - Standalone chibi character sprite
- **`wheel.png`** - Animated futuristic wheel design

**Character Features:**
- Large chibi eyes with highlights
- Curly volumous hair
- Subtle beard
- Peach skin tone
- Striped casual shirt

**Hover-Car Features:**
- Cyan/blue gradient body
- Solar panels on top
- Cockpit window
- Engine exhaust ports
- Futuristic wheel design (cyan glow)
- Yellow accent lights

### Background Assets (`assets/images/backgrounds/`)
- **`space_bg.png`** - Deep space gradient background (dark blue to purple)
- **`stars_layer.png`** - Twinkling stars with cross glows
- **`grid_ground.png`** - Futuristic circuit grid ground
- **`planet_blue.png`** - Earth-like blue planet
- **`planet_red.png`** - Mars-like red planet
- **`planet_purple.png`** - Purple alien planet
- **`planet_pink.png`** - Pink fantasy planet

**Background Features:**
- Parallax scrolling support
- Gradient space atmosphere
- Multiple star layers
- Decorative floating planets
- Futuristic grid ground with circuit patterns

### Enemy Assets (`assets/images/enemies/`)
- **`asteroid_1.png`** to **`asteroid_4.png`** - Varied asteroid sizes
  - Irregular rocky shapes
  - Surface craters
  - Brown/orange color scheme
  - Different sizes (50px - 80px)
  
- **`ufo.png`** - Enemy flying saucer
  - Green saucer body
  - Transparent dome
  - Yellow windows
  - Blue accent lights
  - Classic UFO design

### Power-up Assets (`assets/images/powerups/`)
- **`energy_orb.png`** - Collectible energy orb
  - Golden yellow core
  - Glowing outer aura
  - White sparkle highlight
  - Pulsing animation support
  
- **`shield.png`** - Shield power-up
  - Hexagonal shield shape
  - Cyan/blue colors
  - Transparent with glow effect
  - Inner light pattern

### UI Assets (`assets/images/ui/`)
- **`boost_icon.png`** - Boost/flame indicator icon
  - Orange and yellow flame
  - Stylized fire shape
  - Perfect for HUD display

## 🔧 Asset Generator Usage

### Generate All Assets
```bash
python -m src.asset_generator
```

This will create all game assets in the `assets/images/` directory.

### Programmatic Usage
```python
from src.asset_generator import AssetGenerator

generator = AssetGenerator()

# Generate specific assets
player = generator.create_player_with_car(140, 90)
asteroid = generator.create_asteroid(60)
planet = generator.create_planet(80, 'purple')
background = generator.create_space_background(1920, 720)

# Generate all at once
generator.generate_all_assets()
```

## 🎨 Customization

### Modify Asset Generator
Edit `src/asset_generator.py` to customize:

#### Player Character
```python
def create_chibi_character(self, size=80):
    # Modify colors
    hair_color = (70, 45, 25)      # Dark brown curly hair
    skin_color = (255, 220, 177)    # Peach skin tone
    shirt_stripes = [(70, 130, 180), (245, 222, 179)]  # Blue/beige
```

#### Hover-Car
```python
def create_hover_car(self, width=120, height=60):
    # Modify car colors
    body_colors = [(100, 200, 220), (70, 170, 200)]  # Cyan gradient
    panel_color = (50, 100, 180)   # Solar panel blue
```

#### Enemies
```python
def create_asteroid(self, size):
    # Change asteroid appearance
    base_color = (120, 80, 50)     # Brown rocky color
    crater_color = (90, 60, 40)    # Darker craters

def create_ufo(self, width=70, height=40):
    # Modify UFO design
    body_color = (100, 180, 100)   # Green body
    dome_color = (150, 220, 150)   # Light green dome
```

#### Backgrounds
```python
def create_space_background(self, width, height):
    # Adjust gradient colors
    start_color = (10, 10, 40)     # Deep space blue
    end_color = (60, 30, 90)       # Purple tint

def create_planet(self, size, planet_type='earth'):
    # Add new planet types
    colors = {
        'custom': [(R, G, B), (R, G, B), (R, G, B)]
    }
```

## 🎮 Asset Features

### All Assets Include:
✅ **Transparency support** (RGBA)  
✅ **Scalable** - Can be resized without quality loss  
✅ **Optimized** for game performance  
✅ **Consistent art style** - Chibi/pixel-art aesthetic  
✅ **Animation-ready** - Support for rotation, pulsing, etc.  

### Technical Specs:
- **Format:** PNG with alpha channel
- **Resolution:** Varied (optimized per asset type)
- **Color depth:** 32-bit RGBA
- **Generator:** Pure Python (Pygame)
- **No dependencies** beyond Pygame

## 🚀 Regeneration

To regenerate assets with different styles:

1. **Modify** `src/asset_generator.py`
2. **Delete** old assets (optional):
   ```bash
   rm -rf assets/images/*
   ```
3. **Regenerate**:
   ```bash
   python -m src.asset_generator
   ```

## 📊 Asset Statistics

| Category | Count | Total Size |
|----------|-------|------------|
| Player | 3 files | ~50 KB |
| Backgrounds | 7 files | ~200 KB |
| Enemies | 5 files | ~30 KB |
| Power-ups | 2 files | ~10 KB |
| UI | 1 file | ~5 KB |
| **TOTAL** | **18 files** | **~295 KB** |

## 🎯 Performance Tips

1. **Caching**: Assets are loaded once and reused
2. **Scaling**: Pre-scale assets during load, not every frame
3. **Transparency**: Use `convert_alpha()` for better performance
4. **Sprites**: All sprites support efficient blitting

## 🔮 Future Asset Ideas

- [ ] Animated explosion effects
- [ ] Thruster particle systems
- [ ] More enemy types (meteors, satellites)
- [ ] Collectible coin sprites
- [ ] Power-up trails and effects
- [ ] Animated background nebulas
- [ ] Character expressions (happy, scared)
- [ ] Multiple hover-car skins

## 💡 Tips

### High Quality Output
The generator creates production-ready assets suitable for:
- Game jams
- Indie games
- Prototypes
- Educational projects

### Customization
Every aspect is tweakable - colors, sizes, shapes, effects. The asset generator is your creative toolkit!

### Consistency
All assets share a unified art style that matches your chibi space theme perfectly.

---

**Generated with ❤️ using Python and Pygame**  
*No external graphics software required!*
