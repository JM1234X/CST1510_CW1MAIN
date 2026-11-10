"""Blackjack, object-oriented: the cards and the logic that scores them live on a Hand."""
import random
import sys

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Hand:
    """A player's cards, plus the actions that belong to them."""

    def __init__(self):
        """Start with no cards."""
        self.cards = []

    def add_card(self):
        """Deal one random card into this hand."""
        self.cards.append(random.choice(CARDS))

    def score(self):
        """Return the hand's total (aces count 1 if 11 would bust); 0 means blackjack."""
        total = sum(self.cards)
        if total == 21 and len(self.cards) == 2:
            return 0
        aces = self.cards.count(11)
        while total > 21 and aces:
            total -= 10          # turn one ace from 11 into 1
            aces -= 1
        return total


def compare(user_score, computer_score):
    """Return a message describing the result."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    return "You lose"


def play_game():
    """Play one round of Blackjack using two Hand objects."""
    user_hand = Hand()
    computer_hand = Hand()
    for _ in range(2):
        user_hand.add_card()
        computer_hand.add_card()

    game_over = False
    while not game_over:
        user_score = user_hand.score()
        computer_score = computer_hand.score()
        print(f"  Your cards: {user_hand.cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_hand.cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        elif input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            user_hand.add_card()
        else:
            game_over = True

    while computer_hand.score() != 0 and computer_hand.score() < 17:
        computer_hand.add_card()

    user_score = user_hand.score()
    computer_score = computer_hand.score()
    print(f"  Your final hand: {user_hand.cards}, final score: {user_score}")
    print(f"  Computer's final hand: {computer_hand.cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


def test_hand():
    """Step 5: test Hand on its own, before touching the game loop."""
    h = Hand()
    for _ in range(4):
        h.add_card()
        print(h.cards, h.score())
    fixed = Hand()
    fixed.cards = [11, 10]
    assert fixed.score() == 0            # blackjack
    fixed.cards = [11, 5, 10]
    assert fixed.score() == 16           # ace drops to 1
    fixed.cards = [11, 11, 9]
    assert fixed.score() == 21           # one ace as 11, one as 1
    fixed.cards = [10, 10, 5]
    assert fixed.score() == 25           # bust
    print("Hand tests passed")


if len(sys.argv) > 1 and sys.argv[1] == "--test":
    test_hand()
else:
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n" * 20)
        play_game()
