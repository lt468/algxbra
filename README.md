# algxbra

[![Project Demo Video](https://img.youtube.com/vi/JU4nGN1SDhg/0.jpg)](https://youtu.be/JU4nGN1SDhg)

Welcome to algxbra, a Python-based math game that helps you practice your algebra skills!

## Introduction

This project is my submission for Harvard University's CS50x course, an introduction to computer science. algxbra is a simple yet engaging game that generates algebraic equations for players to solve. It aims to provide an interactive and enjoyable way to enhance algebraic problem-solving abilities. The project's name "algxbra" is pronounced as "Al-jeks-bra."

I designed this project based on my A-level project, which unfortunately I lost the code for. However, I decided to give it another try and recreate it. In the process, I made certain design choices. For example, in `main.py`, I used different functions to easily recall different screens. In `math_questions.py`, I used a set to generate the answers to the questions, ensuring the uniqueness of numbers. However, this caused an infinite loop issue, possibly due to shuffling the set.

For more information about Harvard University's CS50x course, you can visit the [official course page](https://pll.harvard.edu/course/cs50-introduction-computer-science).

**Please note:** algxbra is an open-source project, and you are free to use and modify the code as per the terms of the license.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Interactive main menu screen
- Difficulty selection (Easy, Medium, Hard)
- Timed gameplay with a countdown timer
- Randomly generated arithmetic questions
- Multiple choice options for each question
- Score tracking and high score persistence
- Game over screen with score display and option to play again or return to the main menu

## Requirements
- Python 3.x
- Pygame library
- SQLite database support

## Installation
1. Make sure you have Python 3.x installed on your system. If not, download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

2. Install the Pygame library using pip:

   ```shell
   pip install pygame

## Usage
1. Clone the repository to your local machine or download the source code as a ZIP file and extract it.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to start the game:

   ```shell
   python3 main.py

4. The game will launch, and you will see the main menu screen. Use the mouse to navigate and click on the options.

5. In the options menu, you can select the difficulty level (Easy, Medium, or Hard) by clicking on the respective option.

6. Once the game starts, a math question will be displayed, and you need to select the correct answer from the multiple-choice options.

7. The game has a time limit, and you must answer as many questions as possible within the given time.

8. After the time runs out, the game over screen will be displayed, showing your score and the current high score. You can choose to play again or return to the main menu.

9. You can choose to reset all highscores in the options menu if you wish to do so!

## Contributing
Contributions to algxbra are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
algxbra is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes.

---
