# Formula 1 Simulation V1
A terminal-based Formula 1 championship simulation written in Python.

This project simulates a short Formula 1 season with predefined drivers and tracks, allowing the user to choose a driver and follow the championship race by race directly in the terminal.

---

# Project Objective
The goal of this project is to practice core Python fundamentals while building a complete, closed-scope program from start to finish, with focus on:
- problem decomposition
- function responsibility
- control flow
- basic data structures
- terminal-based user interaction

---

# How the simulation works 
- The user selects one driver.
- The season consists of 3 races, one per predefined track.
- In each race:
    - All drivers receive a performance score based on:
    - driver attributes
    - track attributes
    - a small random luck factor
- Drivers are ranked according to their score.
- Championship points are assigned based on finishing position (25, 18, 15).
- After all races:
    - The final championship standings are calculated.
    - If there is a tie for first place, a tie-breaker race is held.
    - The winner of the tie-breaker is declared the champion.

---

# How to run
You only need Python 3 installed.

From the project folder, run:
```bash
python main.py
```
The program runs entirely in the terminal and guides the user step by step.

---

# Tech stack
- Python 3
- Standard library only (no external dependencies)

---

# Notes
This project was developed as a learning exercise to practice:
- breaking down a problem into clear steps
- separating responsibilities between functions
- managing program flow and state
- designing a clean and understandable terminal user experience
The focus is on clarity, correctness, and structure — not on realism or advanced simulation.

---

# Project structure
The project contains only two files:
- main.py
- README.md

# Limitations
- Does not simulate laps or real race dynamics
- Not a realistic motorsport model
- No team standings

- Designed for learning purposes only
