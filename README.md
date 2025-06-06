# 🐍 Angry Pythons - Ein lustiges Physics-Puzzle-Spiel

Ein unterhaltsames Angry Birds-ähnliches Spiel, entwickelt in Python mit Pygame!

## 📋 Spielkonzept

**Angry Pythons** ist ein lustiges Physics-Puzzle-Spiel, bei dem Spieler verschiedene Python-Schlangen (statt Vögel) mit einer Schleuder auf Strukturen schießen, um alle Code-Bugs (statt Schweine) zu eliminieren. 

### 🎮 Gameplay-Features
- **Verschiedene Python-Typen** mit speziellen Fähigkeiten:
  - **Standard Python**: Normale Flugbahn
  - **Turbo Python**: Beschleunigung während des Flugs
  - **Heavy Python**: Mehr Masse für stärkeren Aufprall
  - **Split Python**: Teilt sich in drei kleinere Pythons
  
- **Lustige Gegner**: Code-Bugs mit verschiedenen Eigenschaften
- **Physik-Engine**: Realistische Bewegungen und Kollisionen
- **Level-System**: Progressiv schwieriger werdende Level
- **Punkte-System**: Basierend auf verursachtem Schaden und verbleibenden Pythons

## 🛠️ Technische Anforderungen

### Kern-Technologien
- **Python 3.8+**
- **Pygame 2.5+**: Für Grafik und Sound
- **Pymunk**: Physik-Engine für realistische Bewegungen
- **JSON**: Für Level-Daten und Spielstände

### Architektur
```
angry-pythons/
├── main.py              # Haupteinstiegspunkt
├── game/                # Spiellogik
│   ├── __init__.py
│   ├── game_manager.py  # Hauptspielschleife
│   ├── physics.py       # Physik-Engine Integration
│   └── level.py         # Level-Management
├── entities/            # Spielobjekte
│   ├── __init__.py
│   ├── python.py        # Python-Schlangen Klassen
│   ├── bug.py           # Bug-Gegner Klassen
│   └── structure.py     # Baustrukturen
├── ui/                  # Benutzeroberfläche
│   ├── __init__.py
│   ├── menu.py          # Hauptmenü
│   ├── hud.py           # In-Game UI
│   └── level_select.py  # Level-Auswahl
├── assets/              # Ressourcen
│   ├── sprites/         # Grafiken
│   ├── sounds/          # Soundeffekte
│   └── levels/          # Level-Definitionen (JSON)
└── utils/               # Hilfsfunktionen
    ├── __init__.py
    ├── config.py        # Spielkonfiguration
    └── helpers.py       # Allgemeine Hilfsfunktionen
```

### Design-Prinzipien
- **Lustig & Verspielt**: Bunte Grafiken, witzige Animationen
- **Intuitiv**: Einfache Maus-Steuerung
- **Progressiv**: Steigende Schwierigkeit
- **Belohnend**: Satisfying Physics und Zerstörungseffekte

## 🎨 Visuelle Gestaltung

### Grafik-Stil
- **Cartoon-artig** mit kräftigen Farben
- **Python-Thema**: Schlangen mit Programming-Twist
- **Lustige Animationen**: Wackelnde Augen, Zungen, etc.

### Sound-Design
- **Komische Soundeffekte**: "Hisss" beim Abschuss
- **Befriedigende Crash-Sounds**: Beim Treffen von Strukturen
- **Fröhliche Hintergrundmusik**: Python-Song Remixes?

## 🚀 Entwicklungsziele

1. **MVP (Minimum Viable Product)**
   - Grundlegende Physik-Engine
   - Eine spielbare Python-Type
   - 5 Tutorial-Level
   - Basis-UI

2. **Erweiterungen**
   - Weitere Python-Typen
   - Power-Ups
   - Level-Editor
   - Highscore-System
   - Achievements

## 📦 Installation & Start

```bash
# Repository klonen
git clone https://github.com/prof-schacht/angry-pythons.git
cd angry-pythons

# Abhängigkeiten installieren
pip install -r requirements.txt

# Spiel starten
python main.py
```

## 🤝 Contributing

Siehe die Issues für aktuelle Aufgaben und Entwicklungsschritte!

## 📄 Lizenz

MIT License - Frei für Bildungszwecke und Spaß!
