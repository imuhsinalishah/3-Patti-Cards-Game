import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Card and deck setup
faces = ["Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck = []

# Create deck
for i in range(52):
    deck.append(faces[i % 13] + " of " + suits[i // 13])

# Initial points for players
player_one_points = 0
player_two_points = 0

# Initialize main window
root = tk.Tk()
root.title("Card Game")
root.geometry("900x600")  # Window size
root.configure(bg="#f0f0f0")  # Background color for the window

# Load background image
bg_image = PhotoImage(file="background_image.png")  # Ensure you have an image file "background_image.g"
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # Set the background image to cover the entire window

# Player points labels
player_one_label = tk.Label(root, text=f"Player One: {player_one_points} points", font=("Arial", 16), bg="#6fa3ef", fg="white", width=30, height=2)
player_one_label.grid(row=0, column=0, columnspan=2, pady=10)

player_two_label = tk.Label(root, text=f"Player Two: {player_two_points} points", font=("Arial", 16), bg="#e57373", fg="white", width=30, height=2)
player_two_label.grid(row=1, column=0, columnspan=2, pady=10)

# Canvas for card display
canvas = tk.Canvas(root, bg="#e3f2fd")
canvas.grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")

# Game result label
result_label = tk.Label(root, text="Game Result", font=("Arial", 14), bg="#f0f0f0")
result_label.grid(row=3, column=0, columnspan=2, pady=20)

# Variables to hold player and PC cards
player_one_cards = []
player_two_cards = []

# Function to shuffle the deck
def shuffle_deck():
    for first in range(len(deck)):
        second = random.randint(0, 51)
        temp = deck[first]
        deck[first] = deck[second]
        deck[second] = temp

# Function to choose random cards for both players
def choose_random():
    global player_one_cards, player_two_cards
    shuffle_deck()
    player_one_cards = [random.choice(deck), random.choice(deck), random.choice(deck)]
    player_two_cards = [random.choice(deck), random.choice(deck), random.choice(deck)]
    
    # Update result label
    result_label.config(text="Cards dealt! Now you can view them.")
    
    # Disable the play button after game starts
    play_button.config(state=tk.DISABLED)

# Function to display card names only
def display_cards(cards):
    card_names = "\n".join(cards)
    canvas.delete("all")  # Clear the canvas before displaying new cards
    canvas.create_text(10, 10, anchor="nw", text="Your Cards:\n" + card_names, font=("Courier", 12), fill="black")

# Function to display player cards when button is clicked
def show_player_cards():
    display_cards(player_one_cards)

# Function to display PC cards when button is clicked
def show_pc_cards():
    display_cards(player_two_cards)

# Function to calculate the rank of a card
def card_rank(card):
    face, suit = card.split(" of ")
    return faces.index(face)

# Helper functions for evaluating the hand
def is_flush(cards):
    suits = [card.split(" of ")[1] for card in cards]
    return suits[0] == suits[1] == suits[2]

def is_sequence(cards):
    ranks = sorted([card_rank(card) for card in cards])
    return ranks[1] == ranks[0] + 1 and ranks[2] == ranks[1] + 1

def is_pair(cards):
    faces = [card.split(" of ")[0] for card in cards]
    return len(set(faces)) == 2

def is_trail(cards):
    faces = [card.split(" of ")[0] for card in cards]
    return len(set(faces)) == 1

def evaluate_hand(cards):
    if is_trail(cards):
        return 1
    elif is_flush(cards) and is_sequence(cards):
        return 2
    elif is_sequence(cards):
        return 3
    elif is_flush(cards):
        return 4
    elif is_pair(cards):
        return 5
    else:
        return 6

# Function to determine the winner
def find_winner():
    global player_one_points, player_two_points
    player_one_rank = evaluate_hand(player_one_cards)
    player_two_rank = evaluate_hand(player_two_cards)

    if player_one_rank < player_two_rank:
        player_one_points += 20
        player_two_points -= 10
        result_label.config(text="Player One Wins! +20 points")
    elif player_two_rank < player_one_rank:
        player_two_points += 20
        player_one_points -= 10
        result_label.config(text="Player Two Wins! +20 points")
    else:
        player_one_high_card = max([card_rank(card) for card in player_one_cards])
        player_two_high_card = max([card_rank(card) for card in player_two_cards])
        
        if player_one_high_card > player_two_high_card:
            player_one_points += 20
            player_two_points -= 10
            result_label.config(text="Player One Wins! +20 points")
        elif player_two_high_card > player_one_high_card:
            player_two_points += 20
            player_one_points -= 10
            result_label.config(text="Player Two Wins! +20 points")
        else:
            result_label.config(text="It's a Tie! No points awarded.")
    
    # Update the points labels
    player_one_label.config(text=f"Player One: {player_one_points} points")
    player_two_label.config(text=f"Player Two: {player_two_points} points")

# Function to reset the game
def play_again():
    global player_one_points, player_two_points, player_one_cards, player_two_cards
    player_one_points = 0
    player_two_points = 0
    player_one_cards = []
    player_two_cards = []
    player_one_label.config(text=f"Player One: {player_one_points} points")
    player_two_label.config(text=f"Player Two: {player_two_points} points")
    result_label.config(text="Game Result")
    canvas.delete("all")  # Clear the canvas
    canvas.create_text(10, 10, anchor="nw", text="Cards will be shown here", font=("Courier", 12), fill="black")
    play_button.config(state=tk.NORMAL)  # Enable the play button again

# Function to shuffle again without changing points
def shuffle_again():
    shuffle_deck()
    result_label.config(text="Deck shuffled! Cards will be dealt again.")
    canvas.delete("all")
    canvas.create_text(10, 10, anchor="nw", text="Cards will be shown here", font=("Courier", 12), fill="black")

# Frame to contain the buttons horizontally (3 in each row)
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=4, column=0, columnspan=2, pady=20)

# Buttons for the game (adjusting size and layout)
button_width = 15
button_height = 2

# Row 1: Play, Shuffle, Show Player Cards
play_button = tk.Button(button_frame, text="Play", font=("Arial", 12), bg="#4caf50", fg="white", width=button_width, height=button_height, command=choose_random)
play_button.grid(row=0, column=0, padx=10, pady=10)

shuffle_button = tk.Button(button_frame, text="Shuffle Again", font=("Arial", 12), bg="#ff9800", fg="white", width=button_width, height=button_height, command=shuffle_again)
shuffle_button.grid(row=0, column=1, padx=10, pady=10)

show_player_button = tk.Button(button_frame, text="Show Your Cards", font=("Arial", 12), bg="#03a9f4", fg="white", width=button_width, height=button_height, command=show_player_cards)
show_player_button.grid(row=0, column=2, padx=10, pady=10)

# Row 2: Show PC Cards, Find Winner, Reset Game
show_pc_button = tk.Button(button_frame, text="Show PC's Cards", font=("Arial", 12), bg="#9e9e9e", fg="white", width=button_width, height=button_height, command=show_pc_cards)
show_pc_button.grid(row=1, column=0, padx=10, pady=10)

find_winner_button = tk.Button(button_frame, text="Find Winner", font=("Arial", 12), bg="#8bc34a", fg="white", width=button_width, height=button_height, command=find_winner)
find_winner_button.grid(row=1, column=1, padx=10, pady=10)

play_again_button = tk.Button(button_frame, text="Reset Game", font=("Arial", 12), bg="#f44336", fg="white", width=button_width, height=button_height, command=play_again)
play_again_button.grid(row=1, column=2, padx=10, pady=10)

# Make the window and canvas resize automatically when content changes
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the GUI main loop
root.mainloop()
