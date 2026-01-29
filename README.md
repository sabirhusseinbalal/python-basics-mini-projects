# 🐍 Python Basics – Mini Projects

A collection of small Python programs to practice basic Python concepts like loops, conditions, functions, and user input.

---

## 📂 Mini Projects

### 1️⃣ Check Leap Year
**File:** `1_Check_Leap_Year.py`

- Checks if a year is a leap year
- Uses standard leap year rules
- User can exit by typing `q`

---

### 2️⃣ Decimal ↔ Binary Converter
**File:** `2_Decimal_to_Binary_&_ViceVersa.py`

- Convert Decimal to Binary
- Convert Binary to Decimal
- Uses manual logic (no built-in shortcuts)
- Validates user input
- Menu-based program

---

### 3️⃣ Calculate Age
**File:** `3_Calculate_Age.py`

- Calculates age from birth date
- Handles leap years correctly
- Shows age in:
  - Years, months, days
  - Total months
  - Total days
  - Weeks, hours, minutes, seconds
- Input validation
- Exit anytime using `q`

---

### 4️⃣ Number Guessing Game
**File:** `4_Number_Guessing_Game.py`

- Classic number guessing game with a twist
- Player has **5 hearts** (lives) per round
- Option to use **3 hints**:
  1. Even or Odd
  2. Number range (±10)
  3. Above or below 50
- Score increases when guessing correctly, decreases when wrong
- Tracks **elapsed time** for each session
- Continuous play until user exits by typing `q`

**How it works:**
1. Game generates a random number (1–100)
2. Player guesses the number
3. Player can request hints if available
4. Score and hearts update dynamically
5. Game resets or ends based on player input

---

### 5️⃣ Fetch Words from File
**File:** `5_Fetch_Words_from_File.py`

- Reads text from a .txt file
- Converts all text to lowercase
- Removes punctuation
- Splits text into words
- Counts word frequency using Counter
- Option to:
  * Show only repeated words
  * Show all words
- Displays result in a sorted table using pandas

**How it works:**
1. User enters full file path
2. Program checks if file exists and is .txt
3. File content is cleaned (lowercase, no punctuation)
4. Words are counted
5. User chooses what to display
6. Results are shown in descending order

---

### 6️⃣ Random Word from File
**File:** `6_Random_Word_from_File.py`

- Reads text from a .txt file
- Converts all text to lowercase
- Removes punctuation
- Splits text into words
- Counts word frequency using Counter
- Option to:
  * Pick a random word from all words
  * Pick a random word from repeated words only
- Prints the selected word randomly
- Continuous selection until user quits with q

**How it works:**
1. User enters full file path
2. Program checks if file exists and is .txt
3. Cleans the text (lowercase, removes punctuation)
4. Splits text into words
5. Finds repeated words
6. User chooses to print from:
  * Only repeated words, or
  * All words
7. Program prints a random word based on choice
8. Loop continues until user exits

---

### 7️⃣ Countdown Timer
**File:** `7_Countdown_Timer.py`

- Interactive countdown timer program
- Supports up to 3 timers running simultaneously
- Each timer has:
  * Custom label
  * Custom countdown duration (in seconds)
- All timers update together in real-time
- Screen refreshes every second for a clean live display
- Displays a message when each timer finishes
- Option to restart and set new timers

**How it works:**
1. User chooses number of timers (1–3)
2. User enters a label and time (in seconds) for each timer
3. Program clears the screen and updates all timers every second
4. When a timer reaches zero, it shows a Time’s up message
5. Program ends when all timers finish, or user chooses to exit

### Clone the repository using the command:
   ```bash
   git clone https://github.com/Sabirhusseinbalal/python-basics-mini-projects.git
   ```


## 🐍 Python Project Roadmap
1. 👉 [Python Basics – Mini Projects](https://github.com/sabirhusseinbalal/python-basics-mini-projects)
2. 👉 [File Handling & OS Automation](https://github.com/sabirhusseinbalal/python-file-system-automation)
3. 👉 [Web, Network & API Automation](https://github.com/sabirhusseinbalal/python-web-network-projects)
4. 👉 [Image, Video & Media Processing](https://github.com/sabirhusseinbalal/python-media-processing)
5. 👉 [Security, Encryption & Utilities](https://github.com/sabirhusseinbalal/python-security-utilities)
6. 👉 [CLI, GUI & Small Apps](https://github.com/sabirhusseinbalal/python-cli-gui-apps)
7. 👉 [Bots & Automation](https://github.com/sabirhusseinbalal/python-bots-automation)
8. 👉 [Advanced Python Projects](https://github.com/sabirhusseinbalal/python-bots-automation)
