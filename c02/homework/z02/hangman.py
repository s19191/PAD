from homework.z02.game import Game


class Hangman(Game):

    def __init__(self):
        super().__init__(2)
        self.wordToGuess = None
        self.mistakes = 0
        self.maxMistakes = 7
        self.guessedLetters = []
        self.lettersToGuess = []

    def start_game(self):
        self._play()

    def _play(self):
        super()._play()
        print('Player 1:')
        self.wordToGuess = input("Type a word to guess: ").strip().upper()
        self.lettersToGuess = set(self.wordToGuess)
        print('\nPlayer 2:')
        while self.mistakes < self.maxMistakes and len(self.lettersToGuess) > 0:
            letter = input('\nType letter: ').strip().upper()
            if len(letter) > 1:
                print('\nIllegal move! To many characters!')
            elif len(letter) == 0:
                print('\nIllegal move! No character detected!')
            elif self.guessedLetters.__contains__(letter):
                print('\nYou already tried that letter!')
            elif self.lettersToGuess.__contains__(letter):
                self.lettersToGuess.remove(letter)
            else:
                self.mistakes += 1
            self.guessedLetters.append(letter)
            self.print_covered_word()
            print(f'\nErrors: {self.mistakes}/{self.maxMistakes}')
        if len(self.lettersToGuess) == 0:
            self.print_covered_word()
            print('\nPlayer 2 won!')
        else:
            print('\nPlayer 1 won!')

    def print_covered_word(self):
        for x in self.wordToGuess:
            if self.guessedLetters.__contains__(x):
                print(x, end='')
            else:
                print("_", end='')


game = Hangman()
game.start_game()
