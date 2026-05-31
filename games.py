import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading


# ══════════════════════════════════════════════════════════════════════════════
#  WORD BANK  (Hangman)
# ══════════════════════════════════════════════════════════════════════════════

WORDS = {
    "Animals":      ["elephant","crocodile","butterfly","giraffe","penguin","dolphin",
                     "kangaroo","cheetah","porcupine","flamingo","chameleon","platypus"],
    "Countries":    ["pakistan","australia","brazil","germany","argentina","indonesia",
                     "portugal","switzerland","netherlands","bangladesh","malaysia","tanzania"],
    "Technology":   ["python","javascript","algorithm","database","encryption","blockchain",
                     "kubernetes","microservice","repository","framework","middleware","compiler"],
    "Sports":       ["basketball","volleyball","badminton","gymnastics","swimming","archery",
                     "skateboard","wrestling","fencing","cricket","football","baseball"],
    "Food":         ["spaghetti","croissant","quesadilla","blueberry","avocado","cinnamon",
                     "chocolate","pineapple","watermelon","strawberry","cauliflower","asparagus"],
}

HINTS = {
    "elephant":"largest land animal","crocodile":"ancient reptile","butterfly":"colourful insect",
    "giraffe":"tallest animal","penguin":"flightless bird","dolphin":"intelligent marine mammal",
    "kangaroo":"Australian marsupial","cheetah":"fastest land animal","porcupine":"covered in quills",
    "flamingo":"stands on one leg","chameleon":"changes colour","platypus":"egg-laying mammal",
    "pakistan":"South Asian country","australia":"island continent","brazil":"largest in S. America",
    "germany":"Central European nation","argentina":"home of tango","indonesia":"archipelago nation",
    "portugal":"birthplace of fado","switzerland":"famous for watches","netherlands":"land of tulips",
    "bangladesh":"delta country","malaysia":"twin towers","tanzania":"Mt. Kilimanjaro",
    "python":"popular programming language","javascript":"language of the web",
    "algorithm":"step-by-step problem solution","database":"organised data store",
    "encryption":"data security technique","blockchain":"distributed ledger",
    "kubernetes":"container orchestration","microservice":"small independent service",
    "repository":"code storage location","framework":"software skeleton","middleware":"between layers",
    "compiler":"translates source code",
    "basketball":"5 vs 5 hoop sport","volleyball":"6 vs 6 net sport","badminton":"shuttlecock sport",
    "gymnastics":"acrobatic sport","swimming":"aquatic sport","archery":"bow and arrow",
    "skateboard":"board with wheels","wrestling":"grappling sport","fencing":"sword sport",
    "cricket":"bat and ball game","football":"world's most popular sport","baseball":"American pastime",
    "spaghetti":"Italian pasta","croissant":"French pastry","quesadilla":"Mexican dish",
    "blueberry":"small blue fruit","avocado":"healthy fat fruit","cinnamon":"spice from bark",
    "chocolate":"from cacao beans","pineapple":"tropical fruit","watermelon":"summer fruit",
    "strawberry":"red berry fruit","cauliflower":"white vegetable","asparagus":"green vegetable",
}


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN APP  — launcher
# ══════════════════════════════════════════════════════════════════════════════

class GameHub(tk.Tk):

    BG     = "#0d0d1a"
    PANEL  = "#13132b"
    CARD   = "#1a1a38"
    ACCENT = "#6366f1"
    ACC2   = "#312e81"
    TEXT   = "#e2e8f0"
    MUTED  = "#64748b"
    GREEN  = "#22c55e"
    RED    = "#ef4444"
    YELLOW = "#f59e0b"
    CYAN   = "#06b6d4"
    BORDER = "#2d2d55"
    FONT   = "Segoe UI"

    def __init__(self):
        super().__init__()
        self.title("Game Hub — Hex Softwares")
        self.geometry("1100x750")
        self.minsize(960, 660)
        self.configure(bg=self.BG)
        self._scores = {"ttt_wins":0,"ttt_draws":0,"ttt_losses":0,
                        "hm_wins":0,"hm_losses":0}
        self._build_launcher()

    # ── launcher ─────────────────────────────────────────────────────────────

    def _build_launcher(self):
        self._clear()

        # header
        hdr = tk.Frame(self, bg=self.PANEL, height=70)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="🎮  GAME HUB", font=(self.FONT, 20, "bold"),
                 bg=self.PANEL, fg=self.TEXT).pack(side="left", padx=24, pady=16)
        tk.Label(hdr, text="Hex Softwares  ·  Python Internship  ·  Task 3",
                 font=(self.FONT, 9), bg=self.PANEL, fg=self.MUTED).pack(side="right", padx=20)

        body = tk.Frame(self, bg=self.BG)
        body.pack(fill="both", expand=True, padx=40, pady=30)

        # score bar
        sf = tk.Frame(body, bg=self.CARD,
                      highlightbackground=self.BORDER, highlightthickness=1)
        sf.pack(fill="x", pady=(0, 24))
        tk.Label(sf, text="🏆  Session Scores",
                 font=(self.FONT, 10, "bold"), bg=self.CARD, fg=self.YELLOW).pack(side="left", padx=16, pady=10)
        self._score_lbl = tk.Label(sf,
            text=self._score_text(),
            font=(self.FONT, 10), bg=self.CARD, fg=self.TEXT)
        self._score_lbl.pack(side="left", padx=10)

        # game cards
        cards_row = tk.Frame(body, bg=self.BG)
        cards_row.pack(fill="both", expand=True)

        self._game_card(cards_row,
            icon="❌⭕", title="Tic-Tac-Toe",
            desc=("Classic 3×3 strategy game.\n"
                  "Play against a smart AI opponent.\n"
                  "Three difficulty levels available.\n"
                  "Track your wins, losses & draws."),
            color=self.CYAN,
            cmd=self._launch_ttt)

        self._game_card(cards_row,
            icon="🪢", title="Hangman",
            desc=("Guess the hidden word letter by letter.\n"
                  "5 categories · 60+ words.\n"
                  "Hints available · 6 wrong guesses.\n"
                  "Animated hangman drawing."),
            color=self.ACCENT,
            cmd=self._launch_hangman)

    def _game_card(self, parent, icon, title, desc, color, cmd):
        f = tk.Frame(parent, bg=self.CARD,
                     highlightbackground=color, highlightthickness=2,
                     cursor="hand2")
        f.pack(side="left", fill="both", expand=True, padx=14, pady=4)
        f.bind("<Button-1>", lambda e: cmd())

        tk.Label(f, text=icon, font=(self.FONT, 48),
                 bg=self.CARD).pack(pady=(30, 8))
        tk.Label(f, text=title, font=(self.FONT, 18, "bold"),
                 bg=self.CARD, fg=color).pack()
        tk.Label(f, text=desc, font=(self.FONT, 10),
                 bg=self.CARD, fg=self.MUTED, justify="center").pack(pady=(10, 20))
        tk.Button(f, text=f"▶  Play {title}",
                  font=(self.FONT, 11, "bold"),
                  bg=color, fg="white", relief="flat", bd=0,
                  padx=24, pady=10, cursor="hand2",
                  command=cmd,
                  activebackground=self.ACC2, activeforeground="white"
                  ).pack(pady=(0, 28))

    def _score_text(self):
        s = self._scores
        return (f"Tic-Tac-Toe:  W {s['ttt_wins']}  D {s['ttt_draws']}  L {s['ttt_losses']}"
                f"        Hangman:  W {s['hm_wins']}  L {s['hm_losses']}")

    def _refresh_scores(self):
        if hasattr(self, "_score_lbl"):
            self._score_lbl.config(text=self._score_text())

    def _clear(self):
        for w in self.winfo_children():
            w.destroy()

    def _launch_ttt(self):
        self._clear()
        TicTacToeGame(self)

    def _launch_hangman(self):
        self._clear()
        HangmanGame(self)


# ══════════════════════════════════════════════════════════════════════════════
#  TIC-TAC-TOE
# ══════════════════════════════════════════════════════════════════════════════

class TicTacToeGame:

    WINS = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    def __init__(self, hub: GameHub):
        self.hub = hub
        self.app = hub
        self.difficulty = tk.StringVar(value="Medium")
        self.player_mark = tk.StringVar(value="X")
        self.board = [""] * 9
        self.game_active = False
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self._build()

    def _build(self):
        h = self.app

        # header
        hdr = tk.Frame(self.app, bg=h.PANEL, height=58)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Button(hdr, text="← Back", font=(h.FONT, 10),
                  bg=h.PANEL, fg=h.MUTED, relief="flat", bd=0,
                  padx=10, cursor="hand2",
                  command=h._build_launcher).pack(side="left", padx=14, pady=14)
        tk.Label(hdr, text="❌⭕  Tic-Tac-Toe",
                 font=(h.FONT, 16, "bold"), bg=h.PANEL, fg=h.TEXT).pack(side="left", padx=8)
        tk.Label(hdr, text="vs Smart AI",
                 font=(h.FONT, 9), bg=h.PANEL, fg=h.MUTED).pack(side="left")

        body = tk.Frame(self.app, bg=h.BG)
        body.pack(fill="both", expand=True, padx=30, pady=18)

        # left — controls
        left = tk.Frame(body, bg=h.CARD, width=220,
                        highlightbackground=h.BORDER, highlightthickness=1)
        left.pack(side="left", fill="y", padx=(0, 20))
        left.pack_propagate(False)

        tk.Label(left, text="⚙  Settings",
                 font=(h.FONT, 11, "bold"), bg=h.CARD, fg=h.CYAN).pack(pady=(20, 10), padx=16, anchor="w")

        tk.Label(left, text="Difficulty", font=(h.FONT, 9),
                 bg=h.CARD, fg=h.MUTED).pack(anchor="w", padx=16)
        for d in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(left, text=d, variable=self.difficulty, value=d,
                           font=(h.FONT, 10), bg=h.CARD, fg=h.TEXT,
                           selectcolor=h.ACC2, activebackground=h.CARD,
                           command=self._new_game).pack(anchor="w", padx=24)

        tk.Frame(left, bg=h.BORDER, height=1).pack(fill="x", padx=14, pady=12)

        tk.Label(left, text="Play as", font=(h.FONT, 9),
                 bg=h.CARD, fg=h.MUTED).pack(anchor="w", padx=16)
        for m in ["X", "O"]:
            tk.Radiobutton(left, text=f"  {m}", variable=self.player_mark, value=m,
                           font=(h.FONT, 10), bg=h.CARD, fg=h.TEXT,
                           selectcolor=h.ACC2, activebackground=h.CARD,
                           command=self._new_game).pack(anchor="w", padx=24)

        tk.Frame(left, bg=h.BORDER, height=1).pack(fill="x", padx=14, pady=12)

        # score
        tk.Label(left, text="🏆  Score",
                 font=(h.FONT, 11, "bold"), bg=h.CARD, fg=h.YELLOW).pack(anchor="w", padx=16)
        self.score_labels = {}
        for label, key, color in [("You (X)", "X", h.CYAN),
                                    ("AI  (O)", "O", h.RED),
                                    ("Draws",   "Draw", h.MUTED)]:
            row = tk.Frame(left, bg=h.CARD); row.pack(fill="x", padx=16, pady=3)
            tk.Label(row, text=label, font=(h.FONT, 10),
                     bg=h.CARD, fg=color, width=10, anchor="w").pack(side="left")
            lbl = tk.Label(row, text="0", font=(h.FONT, 13, "bold"),
                           bg=h.CARD, fg=color)
            lbl.pack(side="right")
            self.score_labels[key] = lbl

        tk.Frame(left, bg=h.BORDER, height=1).pack(fill="x", padx=14, pady=12)

        tk.Button(left, text="🔄  New Game",
                  font=(h.FONT, 10, "bold"),
                  bg=h.ACCENT, fg="white", relief="flat", bd=0,
                  padx=14, pady=8, cursor="hand2",
                  command=self._new_game).pack(fill="x", padx=14, pady=4)
        tk.Button(left, text="🗑️  Reset Scores",
                  font=(h.FONT, 9),
                  bg=h.CARD, fg=h.MUTED, relief="flat", bd=0,
                  padx=14, pady=6, cursor="hand2",
                  command=self._reset_scores).pack(fill="x", padx=14)

        # center — board
        center = tk.Frame(body, bg=h.BG)
        center.pack(side="left", fill="both", expand=True)

        self.status_lbl = tk.Label(center, text="Press  New Game  to start!",
                                   font=(h.FONT, 13), bg=h.BG, fg=h.TEXT)
        self.status_lbl.pack(pady=(10, 14))

        board_frame = tk.Frame(center, bg=h.BORDER)
        board_frame.pack()

        self.buttons = []
        for i in range(9):
            btn = tk.Button(board_frame,
                            text="",
                            font=(h.FONT, 32, "bold"),
                            width=4, height=2,
                            bg=h.CARD, fg=h.TEXT,
                            relief="flat", bd=0,
                            cursor="hand2",
                            activebackground=h.ACC2,
                            command=lambda i=i: self._player_move(i))
            r, c = divmod(i, 3)
            btn.grid(row=r, column=c, padx=3, pady=3)
            self.buttons.append(btn)

        # move history
        tk.Label(center, text="Move History",
                 font=(h.FONT, 9), bg=h.BG, fg=h.MUTED).pack(pady=(18, 4))
        self.history_lbl = tk.Label(center, text="—",
                                    font=(h.FONT, 9), bg=h.BG, fg=h.MUTED,
                                    wraplength=420)
        self.history_lbl.pack()
        self._move_history = []

    # ── game logic ────────────────────────────────────────────────────────────

    def _new_game(self):
        self.board = [""] * 9
        self.game_active = True
        self._move_history = []
        self.history_lbl.config(text="—")
        pm = self.player_mark.get()
        self.player = pm
        self.ai = "O" if pm == "X" else "X"
        for btn in self.buttons:
            btn.config(text="", bg=self.hub.CARD, fg=self.hub.TEXT, state="normal")
        self.status_lbl.config(text=f"Your turn  ({self.player})", fg=self.hub.CYAN)
        if self.player == "O":          # AI goes first
            self.app.after(400, self._ai_move)

    def _player_move(self, idx):
        if not self.game_active or self.board[idx]:
            return
        self._place(idx, self.player)
        self._move_history.append(f"You→{idx+1}")
        self._update_history()
        if self._check_end():
            return
        self.status_lbl.config(text="AI is thinking...", fg=self.hub.YELLOW)
        self._disable_board()
        self.app.after(500, self._ai_move)

    def _ai_move(self):
        if not self.game_active:
            return
        idx = self._best_move()
        self._place(idx, self.ai)
        self._move_history.append(f"AI→{idx+1}")
        self._update_history()
        self._enable_board()
        if not self._check_end():
            self.status_lbl.config(text=f"Your turn  ({self.player})", fg=self.hub.CYAN)

    def _place(self, idx, mark):
        self.board[idx] = mark
        color = self.hub.CYAN if mark == self.player else self.hub.RED
        self.buttons[idx].config(text=mark, fg=color,
                                  bg=self.hub.ACC2, state="disabled")

    def _best_move(self):
        d = self.difficulty.get()
        empty = [i for i, v in enumerate(self.board) if not v]
        if d == "Easy":
            return random.choice(empty)
        if d == "Medium" and random.random() < 0.35:
            return random.choice(empty)
        # minimax (Hard / sometimes Medium)
        best, best_score = None, -999
        for i in empty:
            self.board[i] = self.ai
            score = self._minimax(False, 0, -1000, 1000)
            self.board[i] = ""
            if score > best_score:
                best_score, best = score, i
        return best

    def _minimax(self, is_max, depth, alpha, beta):
        winner = self._winner()
        if winner == self.ai:   return 10 - depth
        if winner == self.player: return depth - 10
        empty = [i for i, v in enumerate(self.board) if not v]
        if not empty: return 0
        if is_max:
            best = -1000
            for i in empty:
                self.board[i] = self.ai
                best = max(best, self._minimax(False, depth+1, alpha, beta))
                self.board[i] = ""
                alpha = max(alpha, best)
                if beta <= alpha: break
            return best
        else:
            best = 1000
            for i in empty:
                self.board[i] = self.player
                best = min(best, self._minimax(True, depth+1, alpha, beta))
                self.board[i] = ""
                beta = min(beta, best)
                if beta <= alpha: break
            return best

    def _winner(self):
        for a, b, c in self.WINS:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def _check_end(self):
        winner = self._winner()
        if winner:
            self.game_active = False
            self._highlight_win(winner)
            if winner == self.player:
                self.scores["X"] += 1
                self.hub._scores["ttt_wins"] += 1
                self.status_lbl.config(text="🎉  You Win!", fg=self.hub.GREEN)
            else:
                self.scores["O"] += 1
                self.hub._scores["ttt_losses"] += 1
                self.status_lbl.config(text="😞  AI Wins!", fg=self.hub.RED)
            self._update_scores()
            return True
        if all(self.board):
            self.game_active = False
            self.scores["Draw"] += 1
            self.hub._scores["ttt_draws"] += 1
            self.status_lbl.config(text="🤝  It's a Draw!", fg=self.hub.YELLOW)
            self._update_scores()
            return True
        return False

    def _highlight_win(self, winner):
        for a, b, c in self.WINS:
            if self.board[a] == self.board[b] == self.board[c] == winner:
                color = self.hub.GREEN if winner == self.player else self.hub.RED
                for i in (a, b, c):
                    self.buttons[i].config(bg=color, fg="white")

    def _update_scores(self):
        self.score_labels["X"].config(text=str(self.scores["X"]))
        self.score_labels["O"].config(text=str(self.scores["O"]))
        self.score_labels["Draw"].config(text=str(self.scores["Draw"]))

    def _reset_scores(self):
        self.scores = {"X":0,"O":0,"Draw":0}
        self._update_scores()

    def _disable_board(self):
        for b in self.buttons:
            if not b["text"]:
                b.config(state="disabled")

    def _enable_board(self):
        for i, b in enumerate(self.buttons):
            if not self.board[i]:
                b.config(state="normal")

    def _update_history(self):
        self.history_lbl.config(text="  ·  ".join(self._move_history))


# ══════════════════════════════════════════════════════════════════════════════
#  HANGMAN
# ══════════════════════════════════════════════════════════════════════════════

HANGMAN_STAGES = [
    # 0 wrong
    ["       ",
     "       ",
     "       ",
     "       ",
     "       ",
     "       ",
     "======="],
    # 1
    ["  +---+",
     "  |   |",
     "      |",
     "      |",
     "      |",
     "      |",
     "======="],
    # 2
    ["  +---+",
     "  |   |",
     "  O   |",
     "      |",
     "      |",
     "      |",
     "======="],
    # 3
    ["  +---+",
     "  |   |",
     "  O   |",
     "  |   |",
     "      |",
     "      |",
     "======="],
    # 4
    ["  +---+",
     "  |   |",
     "  O   |",
     " /|   |",
     "      |",
     "      |",
     "======="],
    # 5
    ["  +---+",
     "  |   |",
     "  O   |",
     " /|\\  |",
     "      |",
     "      |",
     "======="],
    # 6 — dead
    ["  +---+",
     "  |   |",
     "  O   |",
     " /|\\  |",
     " / \\  |",
     "      |",
     "======="],
]

class HangmanGame:

    MAX_WRONG = 6

    def __init__(self, hub: GameHub):
        self.hub = hub
        self.app = hub
        self.category = tk.StringVar(value="Technology")
        self.word = ""
        self.guessed = set()
        self.wrong = 0
        self.game_active = False
        self.scores = {"wins": 0, "losses": 0}
        self._build()

    def _build(self):
        h = self.hub

        # header
        hdr = tk.Frame(self.app, bg=h.PANEL, height=58)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Button(hdr, text="← Back", font=(h.FONT, 10),
                  bg=h.PANEL, fg=h.MUTED, relief="flat", bd=0,
                  padx=10, cursor="hand2",
                  command=h._build_launcher).pack(side="left", padx=14, pady=14)
        tk.Label(hdr, text="🪢  Hangman",
                 font=(h.FONT, 16, "bold"), bg=h.PANEL, fg=h.TEXT).pack(side="left", padx=8)
        tk.Label(hdr, text="Guess the word before it's too late!",
                 font=(h.FONT, 9), bg=h.PANEL, fg=h.MUTED).pack(side="left")

        body = tk.Frame(self.app, bg=h.BG)
        body.pack(fill="both", expand=True, padx=24, pady=16)

        # ── left panel ──
        left = tk.Frame(body, bg=h.CARD, width=200,
                        highlightbackground=h.BORDER, highlightthickness=1)
        left.pack(side="left", fill="y", padx=(0,18))
        left.pack_propagate(False)

        tk.Label(left, text="📂  Category",
                 font=(h.FONT, 11, "bold"), bg=h.CARD, fg=h.ACCENT).pack(pady=(18,8), padx=14, anchor="w")
        for cat in WORDS:
            tk.Radiobutton(left, text=cat, variable=self.category, value=cat,
                           font=(h.FONT, 10), bg=h.CARD, fg=h.TEXT,
                           selectcolor=h.ACC2, activebackground=h.CARD,
                           command=self._new_game).pack(anchor="w", padx=22)

        tk.Frame(left, bg=h.BORDER, height=1).pack(fill="x", padx=12, pady=12)

        tk.Label(left, text="🏆  Score",
                 font=(h.FONT, 11, "bold"), bg=h.CARD, fg=h.YELLOW).pack(anchor="w", padx=14)
        row = tk.Frame(left, bg=h.CARD); row.pack(fill="x", padx=14, pady=4)
        tk.Label(row, text="Wins", font=(h.FONT, 10), bg=h.CARD,
                 fg=h.GREEN, width=8, anchor="w").pack(side="left")
        self.win_lbl = tk.Label(row, text="0", font=(h.FONT, 13, "bold"),
                                bg=h.CARD, fg=h.GREEN)
        self.win_lbl.pack(side="right")
        row2 = tk.Frame(left, bg=h.CARD); row2.pack(fill="x", padx=14, pady=4)
        tk.Label(row2, text="Losses", font=(h.FONT, 10), bg=h.CARD,
                 fg=h.RED, width=8, anchor="w").pack(side="left")
        self.loss_lbl = tk.Label(row2, text="0", font=(h.FONT, 13, "bold"),
                                 bg=h.CARD, fg=h.RED)
        self.loss_lbl.pack(side="right")

        tk.Frame(left, bg=h.BORDER, height=1).pack(fill="x", padx=12, pady=12)
        tk.Button(left, text="🔄  New Game",
                  font=(h.FONT, 10, "bold"),
                  bg=h.ACCENT, fg="white", relief="flat", bd=0,
                  padx=14, pady=8, cursor="hand2",
                  command=self._new_game).pack(fill="x", padx=14, pady=4)
        tk.Button(left, text="💡  Hint",
                  font=(h.FONT, 10),
                  bg=h.CARD, fg=h.YELLOW, relief="flat", bd=0,
                  padx=14, pady=6, cursor="hand2",
                  command=self._show_hint).pack(fill="x", padx=14)

        # ── center ──
        center = tk.Frame(body, bg=h.BG)
        center.pack(side="left", fill="both", expand=True)

        top = tk.Frame(center, bg=h.BG)
        top.pack(fill="x")

        # hangman drawing
        self.hang_lbl = tk.Label(top,
                                 text="\n".join(HANGMAN_STAGES[0]),
                                 font=("Courier New", 16, "bold"),
                                 bg=h.BG, fg=h.TEXT,
                                 justify="left")
        self.hang_lbl.pack(side="left", padx=(10, 30), pady=10)

        # right of drawing
        info = tk.Frame(top, bg=h.BG)
        info.pack(side="left", fill="both", expand=True)

        self.status_lbl = tk.Label(info, text="Press  New Game  to start!",
                                   font=(h.FONT, 14, "bold"),
                                   bg=h.BG, fg=h.TEXT)
        self.status_lbl.pack(anchor="w", pady=(10, 6))

        self.word_lbl = tk.Label(info, text="",
                                 font=("Courier New", 26, "bold"),
                                 bg=h.BG, fg=h.CYAN,
                                 letterSpacing=8)
        self.word_lbl.pack(anchor="w", pady=6)

        self.hint_lbl = tk.Label(info, text="",
                                 font=(h.FONT, 10, "italic"),
                                 bg=h.BG, fg=h.YELLOW)
        self.hint_lbl.pack(anchor="w")

        self.wrong_lbl = tk.Label(info, text="",
                                  font=(h.FONT, 10),
                                  bg=h.BG, fg=h.MUTED)
        self.wrong_lbl.pack(anchor="w", pady=4)

        self.used_lbl = tk.Label(info, text="",
                                 font=(h.FONT, 10),
                                 bg=h.BG, fg=h.MUTED,
                                 wraplength=480, justify="left")
        self.used_lbl.pack(anchor="w")

        # keyboard
        kb_frame = tk.Frame(center, bg=h.BG)
        kb_frame.pack(fill="x", pady=(14, 0))
        self.key_btns = {}
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for row_letters in rows:
            rf = tk.Frame(kb_frame, bg=h.BG)
            rf.pack()
            for ch in row_letters:
                btn = tk.Button(rf, text=ch,
                                font=(h.FONT, 11, "bold"),
                                width=3, height=1,
                                bg=h.CARD, fg=h.TEXT,
                                relief="flat", bd=0,
                                cursor="hand2",
                                activebackground=h.ACC2,
                                command=lambda c=ch: self._guess(c))
                btn.pack(side="left", padx=2, pady=3)
                self.key_btns[ch] = btn

        # bind keyboard
        self.app.bind("<Key>", self._key_press)

    # ── game logic ────────────────────────────────────────────────────────────

    def _new_game(self):
        cat = self.category.get()
        self.word = random.choice(WORDS[cat]).upper()
        self.guessed = set()
        self.wrong = 0
        self.game_active = True
        self.hint_lbl.config(text="")
        self.status_lbl.config(text=f"Category: {cat}", fg=self.hub.TEXT)
        self._refresh_drawing()
        self._refresh_word()
        self._refresh_used()
        self.wrong_lbl.config(text=f"Wrong guesses: 0 / {self.MAX_WRONG}")
        for btn in self.key_btns.values():
            btn.config(bg=self.hub.CARD, fg=self.hub.TEXT, state="normal")

    def _guess(self, letter):
        if not self.game_active or letter in self.guessed:
            return
        self.guessed.add(letter)
        if letter in self.word:
            self.key_btns[letter].config(bg=self.hub.GREEN, fg="white", state="disabled")
        else:
            self.wrong += 1
            self.key_btns[letter].config(bg=self.hub.RED, fg="white", state="disabled")
            self.wrong_lbl.config(text=f"Wrong guesses: {self.wrong} / {self.MAX_WRONG}")
        self._refresh_drawing()
        self._refresh_word()
        self._refresh_used()
        self._check_end()

    def _key_press(self, event):
        ch = event.char.upper()
        if ch in self.key_btns:
            self._guess(ch)

    def _check_end(self):
        if all(c in self.guessed for c in self.word):
            self.game_active = False
            self.scores["wins"] += 1
            self.hub._scores["hm_wins"] += 1
            self.win_lbl.config(text=str(self.scores["wins"]))
            self.status_lbl.config(text="🎉  You Won! Well done!", fg=self.hub.GREEN)
            self.word_lbl.config(fg=self.hub.GREEN)
        elif self.wrong >= self.MAX_WRONG:
            self.game_active = False
            self.scores["losses"] += 1
            self.hub._scores["hm_losses"] += 1
            self.loss_lbl.config(text=str(self.scores["losses"]))
            self.status_lbl.config(text=f"💀  Game Over! Word was: {self.word}", fg=self.hub.RED)
            # reveal word
            self.word_lbl.config(text="  ".join(self.word), fg=self.hub.RED)

    def _refresh_drawing(self):
        stage = min(self.wrong, self.MAX_WRONG)
        color = self.hub.RED if stage == self.MAX_WRONG else self.hub.TEXT
        self.hang_lbl.config(text="\n".join(HANGMAN_STAGES[stage]), fg=color)

    def _refresh_word(self):
        display = "  ".join(
            c if c in self.guessed else ("_" if c != " " else " ")
            for c in self.word)
        self.word_lbl.config(text=display)

    def _refresh_used(self):
        wrong_letters = sorted(c for c in self.guessed if c not in self.word)
        self.used_lbl.config(
            text=f"Wrong letters:  {' '.join(wrong_letters) or '—'}")

    def _show_hint(self):
        if not self.game_active:
            messagebox.showinfo("Hint", "Start a new game first!")
            return
        hint = HINTS.get(self.word.lower(), "No hint available.")
        self.hint_lbl.config(text=f"💡 Hint: {hint}")


# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = GameHub()
    app.mainloop()
