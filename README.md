# Ruined Crown

Ruined Crown is a dark fantasy Strategy / City-Builder / RPG developed using Pygame. Players are reincarnated into a nearly destroyed kingdom with knowledge from another world. The core gameplay involves rebuilding the city, managing trade, capturing territories, and developing technologies. The game features a 2D perspective.

## 🎮 Current Version: 0.0.1b

### Implemented Features
- ✅ Main menu with background image
- ✅ Interactive menu buttons with hover effects
- ✅ Settings menu
- ✅ Screen resolution switching (preset modes)
- ✅ FPS adjustment (30/60/120)
- ✅ Game core module (configuration & state management)

### Tech Stack
- **Language:** Python 3.12+
- **Framework:** Pygame 2.6.1+
- **Platform:** macOS / Windows / Linux

### Project Structure
```
RuinedCrown/ 
├── main.py # Entry point 
├── core/ 
│ └── core.py # Game core (settings, state) 
├── GUI/ 
│ └── GUIMenu.py # Menu & UI components 
└── requirements.txt # Dependencies
```

## 🚧 Development Status
**In Progress** — Currently in early development (alpha stage).

## 📋 Roadmap
- [ ] Character creation screen
- [ ] Game start / world generation
- [ ] City building mechanics
- [ ] Trade system
- [ ] Technology tree
- [ ] Territory capture

## 🛠 Installation
```bash
# Clone the repository
git clone https://github.com/Dmitry2571/RuinedCrown.git
cd RuinedCrown

# Install dependencies
pip3 install -r requirements.txt

# Run the game
python3 main.py
