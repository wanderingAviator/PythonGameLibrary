import rps
import minesweeper
import heavens_gambit
import wordle

def main():
    choice = "-1"

    while (choice != "5"):

        choice = input("Python Game Library\nInput a number to select a game, or enter \"h\" to read the game guides.\n  1. Minesweeper\n  2. Heaven's Gambit  \n  3. Rock Paper Scissors\n  4. Wordle\n  5. Exit Program\n> ").lower()
        match(choice.lower()):

            case "1":
                print("You have chosen: Minesweeper")
                minesweeper.run_game()

            case "2":
                print("You have chosen: Heaven's Gambit")
                heavens_gambit.run_game()
            case "3":
                print("You have chosen: Rock Paper Scissors")
                rps.run_game()

            case "4":
                print("You have chosen: Wordle")
                wordle.run_game()

            case "5":
                print("Exiting Program...")

            case "h":
                print("")
                print("1. Minesweeper")
                print("Description: Uncover as many tiles as you can! You get 1 point per tile you uncover. If you uncover a bomb, you lose!")
                print("Instructions: Enter coordinates to chose a tile to open. Top-Left is 1,1; Bottom-Right is 5,5 6,6 or 8,8 depending on difficulty.")
                print("")
                print("2. Heaven's Gambit")
                print("Description: A slots-like game, with 9 boons granted by the 9 angels of fortune. Win big!")
                print("Instructions: Enter a number to make your offering. The game is over if you lose all your money.")
                print("")
                print("3. Rock Paper Scissors")
                print("Description: A game of luck that can be played against a friend, or a CPU.")
                print("Instructions: Choose your fighter by entering \"r\", \"p\", or \"s\". Rock beats scissors, scissors beats paper, paper beats rock.")
                print("")
                print("4. Wordle")
                print("Description: Guess the 5-letter word in 6 tries or less.")
                print("Instructions: Enter a 5-letter word to make a guess. Capitalized letters are right spot, right letter. Lowercase letters are wrong spot, right letter.")
                print("")

            case _:
                print("Please enter a valid option.")
    
main()