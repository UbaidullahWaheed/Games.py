# 🎮 Game Hub — Tic-Tac-Toe & Hangman

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Games](https://img.shields.io/badge/Games-2%20in%201-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Internship](https://img.shields.io/badge/Hex%20Softwares-Internship-red?style=for-the-badge)

A **premium dark-themed Game Hub** featuring two fully-featured classic games — **Tic-Tac-Toe** with a smart AI opponent and **Hangman** with 60+ words across 5 categories. Built entirely with Python and Tkinter.

---

## 🕹️ Games Included

### ❌⭕ Tic-Tac-Toe

| Feature | Details |
|---------|---------|
| 🤖 **AI Opponent** | Minimax algorithm with Alpha-Beta pruning — unbeatable on Hard |
| 🎯 **Difficulty Levels** | Easy (random) · Medium (mixed) · Hard (perfect play) |
| ✋ **Choose Your Mark** | Play as X or O |
| 🏆 **Score Tracking** | Wins · Draws · Losses per session |
| 🌟 **Win Highlighting** | Winning cells highlighted green (you) or red (AI) |
| 📜 **Move History** | Live log of every move made |

### 🪢 Hangman

| Feature | Details |
|---------|---------|
| 📂 **5 Categories** | Animals · Countries · Technology · Sports · Food |
| 📝 **60+ Words** | Unique words with individual hints for each |
| 🎨 **ASCII Art** | Animated 7-stage hangman drawing |
| ⌨️ **Dual Input** | On-screen keyboard buttons + physical keyboard typing |
| 💡 **Hint System** | One hint available per game |
| 🔴 **Letter Tracking** | Wrong letters highlighted red, correct ones green |
| 🏆 **Score Tracking** | Wins & Losses per session |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x (Tkinter is included by default)

### Run the App
```bash
git clone https://github.com/YOUR_USERNAME/HexSoftwares_Game_Hub.git
cd HexSoftwares_Game_Hub
python games.py
```

---

## 🤖 How the AI Works (Tic-Tac-Toe)

The AI uses the **Minimax algorithm** with **Alpha-Beta pruning**:

- **Minimax** — recursively evaluates all possible game states and picks the optimal move
- **Alpha-Beta pruning** — skips branches that can't affect the result, making it faster
- On **Hard** difficulty the AI plays a **perfect game** — it never loses
- On **Medium** it makes random moves 35% of the time for a fair challenge
- On **Easy** it plays fully randomly

```
Score:  AI wins  → +10 - depth
        You win  → depth - 10
        Draw     → 0
```

---

## 📁 Project Structure

```
HexSoftwares_Game_Hub/
│
├── games.py     # Main application (GameHub + TicTacToe + Hangman)
└── README.md    # Project documentation
```

---

## 🗂️ Word Categories (Hangman)

| Category | Sample Words |
|----------|-------------|
| 🐘 Animals | elephant, butterfly, kangaroo, flamingo, chameleon |
| 🌍 Countries | pakistan, australia, switzerland, indonesia, portugal |
| 💻 Technology | python, algorithm, blockchain, kubernetes, encryption |
| ⚽ Sports | basketball, gymnastics, badminton, archery, wrestling |
| 🍕 Food | spaghetti, croissant, quesadilla, avocado, watermelon |

---

## 🛠️ Built With

- **Python 3** — Core language
- **Tkinter** — GUI framework (built-in)
- **Random** — Word selection & Easy AI moves (built-in)

> ✅ Zero external dependencies — runs out of the box!

---

## 📸 App Preview

```
┌────────────────────────────────────────────────────┐
│  🎮  GAME HUB              Hex Softwares Internship │
│  🏆 Session: TTT W:2 D:1 L:0   Hangman W:3 L:1    │
├───────────────────────┬────────────────────────────┤
│                       │                            │
│      ❌⭕             │         🪢                 │
│   Tic-Tac-Toe         │       Hangman              │
│                       │                            │
│  Smart AI · 3 levels  │  5 categories · 60+ words  │
│                       │                            │
│  [ ▶ Play ]           │  [ ▶ Play ]                │
└───────────────────────┴────────────────────────────┘
```

---

## 👨‍💻 Author
Ubaidullah Waheed
Developed as **Task 3** of the **Hex Softwares Python Programming Internship**.

- 🌐 [Hex Softwares](https://www.hexsoftwares.tech)
- 📧 info@hexsoftwares.tech
- 💼 [LinkedIn — Hex Softwares](https://linkedin.com/company/hex-softwares)

---

## 📄 License

This project is licensed under the **MIT License**.
