# 3-Patti Cards Game

3-Patti is a popular Indian card game often referred to as Teen Patti. This project is a simple implementation of the game using Python and Tkinter for the graphical user interface. The game allows you to play between two players (Player One and Player Two), with features like shuffling the deck, dealing cards, and determining the winner based on hand rankings.

## Features
- **Deal Cards**: Shuffle the deck and deal 3 cards to both players.
- **View Cards**: See the cards for both players and the computer.
- **Winner Calculation**: The winner is determined based on the hand ranking system, which includes:
  - Trail (Three of a Kind)
  - Straight Flush (Sequence of Same Suit)
  - Sequence (Straight)
  - Flush (Same Suit)
  - Pair
  - High Card (If none of the above)
- **Reset the Game**: Reset the points and cards for a fresh game.

## Prerequisites
To run this game, you need to have the following installed:

- Python 3.x
- `tkinter` library (usually comes pre-installed with Python)
- `Pillow` library (used for image processing)

You can install `Pillow` using the following command:

pip install Pillow

How to Run
Clone this repository:

bash
Copy code
git clone https://github.com/imuhsinalishah/3-Patti-Cards-Game.git
Navigate to the project folder:

bash
Copy code
cd 3-Patti-Cards-Game
Run the Python script:

bash
Copy code
python game.py
The game window will open, allowing you to play the 3-Patti game interactively.

Game Interface
Once you run the game, you'll see the following components:

Player Points: Points of both players (Player One and Player Two).
Card Display: A canvas showing the cards dealt to both players.
Buttons:
Play: Start the game by dealing cards to both players.
Shuffle Again: Shuffle the deck without changing the game progress.
Show Player Cards: Display the cards dealt to Player One.
Show PC Cards: Display the cards dealt to Player Two (PC).
Find Winner: Calculate and display the winner based on the hands.
Reset Game: Reset the game to its initial state (points, cards, etc.).
Game Rules
Trail (Three of a Kind): Three cards of the same rank.
Straight Flush: Three cards in a sequence, all of the same suit.
Sequence (Straight): Three cards in a sequence, not necessarily of the same suit.
Flush: Three cards of the same suit, not in sequence.
Pair: Two cards of the same rank.
High Card: If none of the above conditions are met, the highest card wins.



### How this `README.md` is structured:
- **Project Overview**: Introduces the 3-Patti card game and its purpose.
- **Features**: Lists the main functionalities and interactions that the game supports.
- **Prerequisites**: Details the necessary setup to run the game, including the required libraries.
- **How to Run**: Provides step-by-step instructions on how to clone the repository and run the game.
- **Game Interface**: Explains the various sections of the game's graphical interface.
- **Game Rules**: Describes the card hand rankings and how the winner is determined.
- **License**: Specifies that the project is under the MIT License.
- **Acknowledgements**: Credits to the libraries used, such as Tkinter and Pillow.
- **Contact**: Provides an email address for user inquiries.

This `README.md` file will help users understand the functionality, installation, and usage of the 3-Patti Cards Game project.
