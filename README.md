# Formula 1 Simulation V1

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

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
- The season consists of 10 races, one per predefined track.
- In each race:
    - All drivers receive a performance score based on:
    - driver attributes
    - track attributes
    - a small random luck factor
- Drivers are ranked according to their score.
- Championship points are assigned to the top 3 finishing positions: 25 points for 1st, 18 for 2nd, 15 for 3rd, 12 for 4th and 10 for 5th.
- After all races:
    - The final championship standings are calculated.
    - If there is a tie for first place, a tie-breaker race is held.
    - The winner of the tie-breaker is declared the champion.

---

# How to run
You only need Python 3 installed.

From the project folder, run:

python main.py

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
- No team standings (only individual driver championship)
- Designed for learning purposes only

## 📄 License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## 👨‍💻 Connect with me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-salgado-940ab9406)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rafarsc87)

## 👨‍💻 Developed By

Rafael Salgado
*Building Python Backend Applications*
