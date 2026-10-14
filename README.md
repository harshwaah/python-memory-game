```
 __  __ ____ __  __  ___  ______   __  __  ____ _____ ____ _   _ 
|  \/  | ___|  \/  |/ _ \|  _ \ \ / / |  \/  |/ ___|_   _/ ___ | | | |
| |\/| |  _|| |\/| | | | | |_) \ V /  | |\/| | |     | | | |   | |_| |
| |  | | |__| |  | | |_| |  _ < | |   | |  | | |___  | | | |___|  _  |
|_|  |_|____|_|  |_|\___/|_| \_\|_|   |_|  |_|\____| |_|  \____|_| |_|
```

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![GUI Framework](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A clean, modern, and lightweight 4x4 Memory Match card game built in Python using the Tkinter GUI library.

---

## Key Features

* **4x4 Card Grid:** Test your memory with 8 pairs of cards.
* **Real-time Stats:** Built-in move counter and dynamic timer.
* **Non-blocking Callbacks:** Safe timeout handling preventing state conflicts on restart.
* **Zero External Dependencies:** Built purely using Python standard library packages (`tkinter`, `random`, `time`).
* **Visual Feedback:** Color-coded card states for selection, failure, and matches.

---

## Game Rules

1. Click any face-down card to reveal its symbol.
2. Click a second card to find its matching pair.
3. If the symbols match, the cards turn green and remain revealed.
4. If the symbols do not match, they reset face-down after a brief delay.
5. Win the game by matching all 8 pairs in the fastest time and fewest moves possible.

---

## Getting Started

### Prerequisites

* Python 3.8 or higher installed on your system.
* Tkinter package (included by default with standard Python installations on Windows and macOS).

*For Linux users, if Tkinter is not installed:*
```bash
sudo apt-get install python3-tk
```

### Installation & Execution

1. Clone or download the repository:
   ```bash
   git clone https://github.com/your-username/memory-match-game.git
   cd memory-match-game
   ```

2. Run the application:
   ```bash
   python main.py
   ```

---

## File Structure

```
.
├── main.py        # Complete game code and Tkinter application framework
└── README.md      # Documentation
```

---

## License

Distributed under the MIT License. See `LICENSE` for more information.