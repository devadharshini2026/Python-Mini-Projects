# 🎯 Number Guessing Game

**Completion Date:** Nov 2022
**Concepts Covered:** Python Loops | Conditionals | Functions | File Handling | Random Module  

---

## 🔹 Project Overview

This is an **interactive number guessing game** built in Python.  
The program generates a random number between **1 and 100**, and the player must guess it.  
Each successful game is **saved in a history file**, allowing players to track their progress over time.

---

## 🔹 Features

| Feature | Description |
|---------|-------------|
| Random Number | Secret number changes every game using Python's `random` module |
| Game History | Each successful attempt is saved in `history.txt` |
| Replay Option | Players can play multiple rounds without restarting |
| Commands | `history` to view past games, `exit` to quit the game |
| Error Handling | Invalid input is safely handled |

---

## 🔹 Example Usage
```
Enter your guess: 50
Too high! Try again.
Enter your guess: 30
Too low! Try again.
Enter your guess: 37
Congratulations! You guessed it in 3 attempts.

