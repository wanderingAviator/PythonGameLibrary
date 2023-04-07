import random
import logger
import time


# main
def run_game():

    keep_playing = "y"
    bank = 1000 #total money
    roll = 0 #number to come up on slots
    bet = 0 #money to bet
    wins = 0 #how many rolls "count" as a win
    losses = 0 #how many rolls "count" as a loss
    jackpot = 0 #how many times "The Favored" was rolled
    reroll = -1 #pity mechanic: chance to get a special case is 9/999
    status = "l" #tracks if last game was a win or loss for "The Equilibrium"
    start_time = time.time()

    print("Starting Bank: $" + str(bank))
    while (keep_playing == "y"):

        if(reroll == -1):
            bet = input("Enter your bet quantity. \n> ")
            while(not validate(bet, bank)):
                bet = input("Please enter a valid quantity. \n> ")

        roll = random.randint(1, 999)

        match(roll):
            case 111:
                print("111: [The Intuitive] Lose half your bet! (-$" + str(int((int(bet) / 2))) + ")")
                bank = bank - int(int(bet) / 2)
                status = "l"
                losses = losses + 1
                reroll = -1

            case 222: 
                print("222: [The Opportunistic] Double your bank, then lose your bet! (+$" + str(bank - int(bet)) + ")")
                bank = (bank * 2) - int(bet)
                status = "w"
                wins = wins + 1
                reroll = -1

            case 333:
                if(status == "w"):
                    print("333: [The Equilibrium] If your previous game was a loss, win your bet, and vice versa! (-$" + bet + ")")
                    bank = bank - int(bet)
                    status = "l"
                    losses = losses + 1
                    reroll = -1
                else:
                    print("333: [The Equilibrium] If your previous game was a loss, win your bet, and vice versa! (+$" + bet + ")")
                    bank = bank + int(bet)
                    status = "w"
                    wins = wins + 1
                    reroll = -1

            case 444:
                if(bank - int(bet) < 200):
                    print("444: [The Guardian] Lose your bet, unless it knocks your bank under $200! (No net gain or loss!)")
                    status = "l"
                    losses = losses + 1
                    reroll = -1
                else:
                    print("444: [The Guardian] Lose your bet, unless it knocks your bank under $200! (-$" + bet + ")")
                    bank = bank - int(bet)
                    status = "l"
                    losses = losses + 1
                    reroll = -1

            case 555:
                print("555: [The Dynamic] Your bank is now what you rolled! (New bank = $555)")
                bank = 555
                status = "w"
                wins = wins + 1
                reroll = -1

            case 666:
                print("666: [The Gambler] Your bank is now your bet! (New bank = $" + bet + ")")
                bank = int(bet)
                status = "l"
                losses = losses + 1
                reroll = -1

            case 777:
                print("777: [The Favored] Jackpot! +$10,000 (Bank: $" + str(bank + 10000) + ")")
                bank = bank + 10000
                status = "w"
                wins = wins + 1
                reroll = -1

            case 888:
                print("888: [The Immutable] Your bank is now the average of your bank prior to this bet, and your bet! (- $" + str(bank - (bank + int(bet)) / 2) + ")")
                bank = (bank + int(bet)) / 2
                status = "l"
                losses = losses + 1
                reroll = -1

            case 999:
                print("999: [The Renewed] Start over! (Bank = $1000)")
                bank = 1000
                status = "w"
                wins = wins + 1
                reroll = -1

            case _:
                if(reroll > 9): #rerolls up to 10 times before declaring a loss
                    print(str(roll) + ": Better luck next time! (-$" + bet + ")")
                    bank = bank - int(bet)
                    status = "l"
                    losses = losses + 1
                    reroll = -1
                else:
                    reroll = reroll + 1

        if(reroll == -1):
            print("Bank: $" + str(bank))

            if(bank <= 0):
                print("Game Over: You're out of money!")
                keep_playing = "n"

            if(keep_playing != 'n'):
                keep_playing = input("Would you like to keep playing? (y/n)\n> ").lower()
                while(keep_playing != "y" and keep_playing != "n"):
                    keep_playing = input("Please enter a valid response. \n> ").lower()

    end_time = time.time()
    logger.log("[Heaven's Gambit] User spent " + logger.time_format(end_time - start_time) + " gambling with " + str(wins) 
               + " wins, " + str(losses) + " losses," + " and stopped with $" + str(bank) + "!")
    
# makes sure a bet is an integer value between 1 and the user's total money
def validate(bet, bank):
    try:
        int(bet)
        if (int(bet) > 0 and int(bet) <= bank):
            return True
        else:
            raise Exception
        
    except:
        return False
    
    