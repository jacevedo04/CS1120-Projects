# Project No.: 2
# Author: Jayden Acevedo-Penny
# Description: Boggle board game

#calling in necessary files and modules
import random
from board import BoggleBoard

#creating the main game
def main():
    #asking the user for a seed and creating the board
    user_seed = int(input('Enter seed: '))
    game_seed = random.seed(user_seed)
    game_board = BoggleBoard(game_seed)
    game_board.display_board()

    #looping the game until the user chooses to exit
    continue_game = True
    while continue_game == True:
        print()
        user_word = input("Enter word (in UPPERcase): ")
        if user_word == "exit":
            break

        #checking to see if user's word is in the board
        if game_board.find_word(user_word):
            print('Correct')
        else:
            print("I don't see that word")

        #checking to see if the user word is a palindrome
        if game_board.is_palindrome(user_word):
            print('this word is a palindrome')
        else:
            print('this word is not a palindrome')

#calling the main function
main()


