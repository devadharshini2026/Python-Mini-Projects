# 🔐 Password Strength Checker

**Completion Date:** 05/12/2022  
**Concepts Covered:** Python Functions | Loops | Conditionals | Regex | File Handling | CLI Applications  

---

## 🔹 Project Overview

A **command-line tool** that evaluates the strength of passwords.  
It checks for **length, lowercase, uppercase, digits, and special characters**, then classifies the password as **Weak, Moderate, or Strong**.  

All password checks are **saved in a history file**, making it easy to review previous attempts.

---

## 🔹 Features

| Feature | Description |
|---------|-------------|
| Length Check | Minimum 8 characters required |
| Character Variety | Checks lowercase, uppercase, digits, and special characters |
| Strength Classification | Weak, Moderate, Strong based on criteria met |
| History Tracking | Each check is saved in `history.txt` |
| Commands | `history` to view previous checks, `exit` to quit |
| Interactive CLI | Clear instructions and criteria feedback |

---

## 🔹 Example Usage
```
Enter password: Dev@123
Password Strength: Moderate
Criteria Check:
✓ Minimum 8 characters
✓ Lowercase letter present
✓ Uppercase letter present
✓ Digit present
✗ Special character missing


