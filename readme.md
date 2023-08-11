<h2 align="center">typing speed test</h2>

The code imports 📦 necessary libraries like curses 🎭, time ⏱, and random 🎲

It defines helper functions like start_screen() 👋 to display a welcome screen, display_test() 🖥 to display the test
text, target text, current typed text, WPM, accuracy etc.

load_text() 📄 loads a random 🎲 text snippet from a text file 📄 to use as the target text.

The main game logic 🎮 is in wpm_test(). It starts a timer ⏱, enters a loop 🔁 to get keypresses ⌨️, calculates WPM based
on characters typed 🤹‍♂️, displays updated stats 📊 after each keypress, checks for completion of target text ✅. It uses
colors 🎨 to indicate correct 🟩 and wrong ❌ characters.

The main() 💻 function initializes colors 🎨, calls the start screen 👋, and runs the game loop 🔁 calling wpm_test() in a
loop until user presses Esc key ⎌.

Overall, it implements a full typing speed test game 🎮 with features like target text 🎯, timer ⏱, WPM calculation 🧮,
accuracy 🎯, color hints 🎨 etc. The code is structured into reusable functions 🔨 and uses curses 🎭 for display and
keyboard ⌨️ input.


---



### my Email :  yossefsabry66@gmail.com
