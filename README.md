# Quizzler

Quizzler is a quiz application that allows users to answer a series of true or false questions related to computer science. The questions are sourced from the Open Trivia Database, and the user's score is tracked throughout the quiz.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files and Classes](#files-and-classes)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/quizzler.git

2. Navigate to the project directory:
   cd quizzler

3. Install the required dependencies:
   pip install requests

## Usage

Run the main script to start the quiz:

python main.py

Answer the questions as they appear on the screen by selecting either "True" or "False". Your score will be displayed at the end of the quiz.

## Files and Classes

- `question_model.py`: Contains the `Question` class, which represents a single question with its text and correct answer.
- `quiz_brain.py`: Contains the `QuizBrain` class, responsible for managing the quiz logic, including tracking the current question, score, and checking answers.
- `ui.py`: Contains the `QuizInterface` class, which handles the graphical user interface using Tkinter.
- `data.py`: Contains the `question_data`, a list of questions and answers.
- `main.py`: The main entry point for the application, where the quiz is initialized and run.

### Class Descriptions

- `Question`: Represents a single question with its text and correct answer.
- `QuizBrain`: Manages the quiz logic, including tracking the current question, score, and checking answers.
- `QuizInterface`: Handles the graphical user interface using Tkinter.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.
