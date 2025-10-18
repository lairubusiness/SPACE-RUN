# 🎮 SPACE RUN - Advanced Character Development System

## 📋 Overview

The game now features a complete **RPG-style character development system** with:

### Core Features
| Feature | Description |
|---------|-------------|
| 🎨 **Animated Sprites** | 4 animation sets (idle, run, jump, boost) with 8 frames each |
| ⭐ **Leveling System** | Gain XP from distance and level up to earn skill points |
| 🌳 **Skill Tree** | 6 upgradeable skills affecting gameplay |
| 🔓 **Abilities** | Unlock special abilities like Double Jump and Dash |
| ⚡ **Energy System** | Manage energy for boost ability |
| 💾 **Persistence** | Save character progress between sessions |
| ✨ **Particle Effects** | Advanced visual feedback for actions |

---

## 🎯 Character Attributes

### Movement Attributes
```python
Speed:        8.0 base → up to 23.0 (max upgraded)
Jump Power:   600 base → up to 1100 (max upgraded)
Boost Power:  1.5x base → up to 3.0x (max upgraded)
Air Control:  70% (better control in mid-air)
```

### Energy System
```python
Max Energy:     100 base → up to 300 (max upgraded)
Energy Regen:   5/sec base → up to 15/sec (max upgraded)
Boost Cost:     20 energy per activation
```

---

## 🌳 Skill Tree

### 1. ⚡ Speed Skill
- **Max Level:** 10
- **Cost:** 1 skill point per level
- **Effect:** +1.5 movement speed per level
- **Total Benefit:** +15.0 speed at max level

### 2. 🦘 Jump Skill  
- **Max Level:** 10
- **Cost:** 1 skill point per level
- **Effect:** +50 jump power per level
- **Total Benefit:** +500 jump power at max level
- **Special:** Unlocks **Double Jump** at level 5

### 3. 🚀 Boost Skill
- **Max Level:** 10
- **Cost:** 1 skill point per level
- **Effect:** +0.15x boost multiplier per level
- **Total Benefit:** +1.5x boost power at max level
- **Special:** Unlocks **Dash** ability at level 5

### 4. ⚙️ Energy Skill
- **Max Level:** 10
- **Cost:** 1 skill point per level
- **Effect:** +20 max energy & +1 regen per level
- **Total Benefit:** +200 max energy, +10 regen/sec at max level

### 5. 🛡️ Shield Skill
- **Max Level:** 5
- **Cost:** 2 skill points per level
- **Effect:** +0.5 seconds shield duration per level
- **Total Benefit:** +2.5 seconds shield time at max level
- **Special:** Unlocks **Shield Regen** at level 3

### 6. 🧲 Magnet Skill
- **Max Level:** 5
- **Cost:** 2 skill points per level
- **Effect:** Increases coin collection range
- **Special:** Unlocks **Coin Magnet** at level 2

---

## 🔓 Unlockable Abilities

### Double Jump
- **Requirement:** Jump Skill Level 5
- **Effect:** Jump again while in mid-air
- **Usage:** Press SPACE a second time while airborne

### Dash
- **Requirement:** Boost Skill Level 5
- **Effect:** Longer boost duration and higher speed multiplier
- **Usage:** Automatic when using boost

### Shield Regen
- **Requirement:** Shield Skill Level 3
- **Effect:** Shield power-ups last longer
- **Benefit:** Better protection from obstacles

### Coin Magnet
- **Requirement:** Magnet Skill Level 2
- **Effect:** Automatically attract nearby coins/orbs
- **Benefit:** Easier collection without precise positioning

---

## ⭐ Leveling System

### XP Gain
- **Distance XP:** Earn XP based on distance traveled
- **Calculation:** `XP = speed * time * 0.1`
- **Bonus XP:** Score converts to XP at game over

### Level Up
- **XP Required:** `100 * (1.2 ^ (level - 1))`
- **Rewards per Level:**
  - +2 Skill Points
  - +10 Max Energy
  - Full energy restore

### Example Progression
```
Level 1:  0 → 100 XP
Level 2:  0 → 120 XP
Level 3:  0 → 144 XP
Level 5:  0 → 207 XP
Level 10: 0 → 516 XP
```

---

## 🎨 Animation System

### Animation States
1. **Idle** - Standing still (8 frames)
2. **Run** - Moving forward (8 frames)
3. **Jump** - In the air (4 frames)
4. **Boost** - Using boost ability (8 frames)

### Animation Features
- **Smooth transitions** between states
- **Bobbing motion** for idle/run
- **Arm swinging** during run
- **Forward lean** during boost
- **Dynamic eye movement**

### Sprite Details
- **Resolution:** 220x140 pixels
- **Format:** PNG with transparency
- **Frames:** 28 total animation frames
- **Location:** `assets/images/player/animations/`

---

## ⚡ Energy Management

### Energy Uses
| Action | Cost | Effect |
|--------|------|--------|
| Boost | 20 | Speed multiplier for 2+ seconds |
| Shield | 0 | Passive protection (from power-up) |

### Energy Regeneration
- **Base Rate:** 5 energy/second
- **Upgraded Rate:** Up to 15 energy/second
- **Full Recharge:** ~7-20 seconds (depends on upgrades)

### Strategy Tips
- Save energy for difficult sections
- Upgrade energy skills for more frequent boosts
- Use boost on straight paths for maximum distance

---

## 💾 Progression Saving

### What Gets Saved
✅ Character Level  
✅ Current XP  
✅ Skill Points  
✅ All Skill Levels  
✅ Unlocked Abilities  
✅ Statistics (distance, jumps, etc.)  
✅ High Score  

### Save Location
`data/save_data.json`

### Manual Save
- Automatically saves on:
  - Level up
  - Skill upgrade
  - Game over
  - Exiting upgrade screen

---

## 🎮 Controls

### Basic Controls
| Key | Action |
|-----|--------|
| SPACE | Jump (Double Jump if unlocked) |
| SHIFT | Boost (uses energy) |
| U | Open Upgrade Screen |
| ESC | Pause / Close Upgrade Screen |
| Q | Quit to Menu (when paused) |

### Upgrade Screen
- **Click** on skill box to upgrade
- **Hover** to see skill info
- **ESC** to close and return to game

---

## 📊 Statistics Tracking

The game tracks your performance:

```python
Total Distance:    Cumulative meters traveled
Total Jumps:       Number of jumps performed
Total Boosts:      Number of boosts activated
Enemies Dodged:    Obstacles avoided with shield
Coins Collected:   Power-ups and orbs gathered
```

View stats in the upgrade screen!

---

## 🎯 Optimal Build Strategies

### Speed Runner Build
Focus on **Speed** and **Boost** skills
- Max out Speed (10)
- Max out Boost (10)
- Minimal Energy investment
- **Goal:** Cover maximum distance quickly

### Survivalist Build
Focus on **Shield** and **Energy**
- Max out Shield (5)
- Max out Energy (10)
- Moderate Jump (5)
- **Goal:** Last longer with protection

### Balanced Build
Equal investment across all skills
- Level 5-6 in all basic skills
- All abilities unlocked
- **Goal:** Versatile gameplay

### Collection Build
Focus on **Magnet** for high scores
- Max out Magnet (5)
- High Energy for frequent boosts
- **Goal:** Maximize coin collection

---

## 🌟 Advanced Tips

### Mastering Double Jump
1. Use first jump to clear low obstacles
2. Save second jump for emergencies
3. Combine with boost for maximum distance

### Energy Conservation
- Don't boost constantly
- Wait for energy to regenerate
- Time boosts for obstacle-free sections

### Skill Point Allocation
- Start with Speed and Jump (most impactful)
- Unlock abilities early (level 5 requirements)
- Save expensive skills (Shield, Magnet) for later

### XP Farming
- Longer runs = more XP
- Use shield to extend runs
- Boost duration adds to XP multiplier

---

## 🔧 Advanced Features

### Particle System
- **Level Up:** Gold particles explosion
- **Jump:** Gray dust clouds
- **Boost:** Orange flame trail
- **Collect:** Yellow sparkles

### Visual Feedback
- **Pulsing** skill point notification
- **Color-coded** skill availability
- **Animated** energy bar
- **Dynamic** XP progress bar

### Physics Improvements
- Better air control
- Momentum preservation
- Smooth acceleration/deceleration
- Realistic gravity

---

## 🎬 How to Play

### 1. Start Game
```bash
python main_advanced.py
```

### 2. First Run
- Play to earn XP
- Level up to get skill points
- Die to bank XP as levels

### 3. Upgrade
- Press **U** to open upgrade screen
- Click skills to spend points
- Close with **ESC** and keep playing

### 4. Unlock Abilities
- Reach skill level 5 (Jump/Boost)
- Unlock powerful new mechanics
- Dominate the game!

### 5. Master the Game
- Experiment with builds
- Find your playstyle
- Achieve high scores
- Max out all skills!

---

## 📈 Progression Timeline

### Early Game (Levels 1-5)
- Focus on basic movement
- Learn jump timing
- Unlock first ability

### Mid Game (Levels 6-15)
- Build your specialization
- All abilities unlocked
- Consistent high scores

### Late Game (Levels 16-30)
- Max out preferred skills
- Perfect gameplay mechanics
- Challenge high scores

### End Game (Level 30+)
- All skills maxed
- Master-level gameplay
- Infinite scaling challenge

---

## 🎨 Customization

### Regenerate Animations
```bash
python -m src.advanced_sprite_generator
```

Creates new animation frames with:
- Different character poses
- Custom colors
- Unique effects

### Modify Stats
Edit `src/character_development.py`:
```python
self.speed = 8.0  # Base speed
self.jump_power = 600.0  # Base jump
self.max_energy = 100  # Starting energy
```

---

## 🏆 Achievements (Ideas)

- **First Steps:** Reach Level 5
- **Speedster:** Max out Speed skill
- **Air Master:** Perform 100 double jumps
- **Survivor:** Travel 10,000 meters in one run
- **Completionist:** Unlock all abilities
- **Legend:** Reach Level 30

---

## 🚀 Next Steps

Your character development system includes:
✅ Complete animation pipeline  
✅ RPG progression mechanics  
✅ Visual upgrade interface  
✅ Particle effects system  
✅ Save/load functionality  
✅ Statistics tracking  

**Ready to play the advanced version!**

```bash
python main_advanced.py
```

---

*Enjoy your enhanced SPACE RUN experience with full character development!* 🎮✨
