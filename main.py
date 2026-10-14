import random
import time
import tkinter as tk

# Game settings
ROWS = 4
COLS = 4

SYMBOLS = ["🍎", "🐱", "🌟", "🎈", "🍕", "🐼", "⚽", "🌈"]

BG_COLOR = "#20243A"
CARD_COLOR = "#444B70"
MATCH_COLOR = "#3A9D78"


class MemoryGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")
        self.root.geometry("500x700")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.moves = 0
        self.matches = 0
        self.first_card = None
        self.second_card = None
        self.locked = False
        self.game_over = False
        self.start_time = None
        self.timer_id = None
        self.hide_id = None

        # Title
        tk.Label(
            root,
            text="MEMORY MATCH",
            font=("Arial", 24, "bold"),
            bg=BG_COLOR,
            fg="white",
        ).pack(pady=15)

        # Scoreboard
        self.info = tk.Label(
            root,
            text="Moves: 0     Matches: 0/8",
            font=("Arial", 13),
            bg=BG_COLOR,
            fg="white",
        )
        self.info.pack(pady=5)

        self.timer_label = tk.Label(
            root,
            text="Time: 0 sec",
            font=("Arial", 12),
            bg=BG_COLOR,
            fg="#FFD166",
        )
        self.timer_label.pack(pady=5)

        # Card grid
        self.board = tk.Frame(root, bg=BG_COLOR)
        self.board.pack(pady=15)

        # Status label created BEFORE calling new_game()
        self.status = tk.Label(
            root,
            text="Find all matching pairs!",
            font=("Arial", 12),
            bg=BG_COLOR,
            fg="white",
        )
        self.status.pack(pady=5)

        self.buttons = []

        # Restart button
        tk.Button(
            root,
            text="New Game",
            font=("Arial", 12, "bold"),
            bg="#FFD166",
            fg="#20243A",
            command=self.new_game,
        ).pack(pady=10)

        # Start initial game
        self.new_game()

    def new_game(self):
        # Cancel pending callbacks from the old game
        for job in (self.timer_id, self.hide_id):
            if job is not None:
                self.root.after_cancel(job)

        self.timer_id = None
        self.hide_id = None

        # Reset game variables
        self.moves = 0
        self.matches = 0
        self.first_card = None
        self.second_card = None
        self.locked = False
        self.game_over = False
        self.start_time = None

        # Shuffle 8 pairs
        self.cards = SYMBOLS * 2
        random.shuffle(self.cards)

        # Remove old cards
        for widget in self.board.winfo_children():
            widget.destroy()

        self.buttons = []

        # Create 4 x 4 grid
        for i in range(ROWS * COLS):
            button = tk.Button(
                self.board,
                text="?",
                font=("Arial", 22, "bold"),
                width=4,
                height=2,
                bg=CARD_COLOR,
                fg="white",
                activebackground="#65709C",
                command=lambda index=i: self.flip_card(index),
            )

            button.grid(
                row=i // COLS, column=i % COLS, padx=5, pady=5
            )

            self.buttons.append(button)

        self.info.config(text="Moves: 0     Matches: 0/8")
        self.timer_label.config(text="Time: 0 sec")
        self.status.config(text="Find all matching pairs!")

    def flip_card(self, index):
        if self.locked or self.game_over:
            return

        # Ignore already revealed or matched cards
        if self.buttons[index]["text"] != "?":
            return

        # Start timer on first move
        if self.start_time is None:
            self.start_time = time.time()
            self.update_timer()

        # Reveal selected card
        self.buttons[index].config(text=self.cards[index], bg="#65709C")

        if self.first_card is None:
            self.first_card = index
            return

        self.second_card = index
        self.moves += 1

        self.info.config(
            text=f"Moves: {self.moves}     Matches: {self.matches}/8"
        )

        # Check whether the cards match
        if self.cards[self.first_card] == self.cards[self.second_card]:
            self.buttons[self.first_card].config(bg=MATCH_COLOR)
            self.buttons[self.second_card].config(bg=MATCH_COLOR)

            self.matches += 1
            self.first_card = None
            self.second_card = None

            self.info.config(
                text=f"Moves: {self.moves}     Matches: {self.matches}/8"
            )

            if self.matches == 8:
                self.game_over = True
                elapsed = int(time.time() - self.start_time)
                self.status.config(
                    text=f"You won in {self.moves} moves!"
                )
                self.timer_label.config(text=f"Time: {elapsed} sec")

        else:
            # Temporarily prevent further clicks
            self.locked = True
            self.status.config(text="Not a match! Try again.")

            self.hide_id = self.root.after(800, self.hide_cards)

    def hide_cards(self):
        # Hide unmatched cards
        for index in (self.first_card, self.second_card):
            self.buttons[index].config(text="?", bg=CARD_COLOR)

        self.first_card = None
        self.second_card = None
        self.locked = False
        self.hide_id = None
        self.status.config(text="Find all matching pairs!")

    def update_timer(self):
        if self.start_time is None or self.game_over:
            return

        elapsed = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed} sec")

        self.timer_id = self.root.after(1000, self.update_timer)


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()