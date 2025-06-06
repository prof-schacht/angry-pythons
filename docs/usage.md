# Angry Pythons - Usage Guide

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- uv (for environment management)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/prof-schacht/angry-pythons.git
cd angry-pythons
```

2. Create a virtual environment with uv:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Running the Game

To start the game, simply run:
```bash
python main.py
```

This will open a window with a sky blue background. Currently, this is just the basic setup - game features will be added in subsequent updates.

## Development Status

### Completed Features
- ✅ Basic project structure
- ✅ Pygame window initialization
- ✅ Configuration system

### Upcoming Features
- Physics engine integration
- Python snake entities
- Bug enemies and structures
- Level system
- Game mechanics
- UI and menus
- Assets and sound effects