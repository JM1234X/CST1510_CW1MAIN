"""Interactive Hangman game."""
import random
WORDS = ['python', 'security', 'network', 'strings', 'forensics']
def play():
    word = random.choice(WORDS)
    guesses = set()
    lives = 6
    while lives > 0:
        display = ' '.join(ch if ch in guesses else '_' for ch in word)
        print(f'{display} | lives: {lives}')
        if all(ch in guesses for ch in word):
            print('You win!'); return
        guess = input('Guess one letter: ').strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print('Enter one letter.'); continue
        if guess in guesses:
            print('Already guessed.'); continue
        guesses.add(guess)
        if guess not in word: lives -= 1
    print(f'Game over. Word: {word}')
if __name__ == '__main__': play()
