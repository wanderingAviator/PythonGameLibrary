import random
import logger
import time

#processes player two's choice, whether P2 is a bot or not
# which: p or c, based on whether P2 is a player or cpu
def player_two_chooses(which):
    if(which == 'p'): #human player
        otherinput = input("P2: Rock(r), Paper(p), or Scissors(s)? \n> ").lower()
        
        while(otherinput != "r" and otherinput != "p" and otherinput != "s"):
            print("Input must be 'r', 'p', or 's'.")
            otherinput = input("P2: Rock(r), Paper(p), or Scissors(s)? \n> ").lower()

        return otherinput
    else: #cpu player
        cpuoptions = ["r", "p", "s"]
        return cpuoptions[random.randint(0,2)]

# main
def run_game():

    p_one_score = 0
    p_two_score = 0
    ties = 0
    start_time = time.time()

    totalloop = "y"

    while(totalloop != "n"):

        playertype = input("P1: Verse a friend(p), or a CPU?(c) \n> ").lower()
        
        while(playertype != "c" and playertype != "p"):
            print("Input must be 'p', or 'c'.")
            playertype = input("P1: Verse a friend(p), or a CPU?(c) \n> ").lower()

        userinput = input("P1: Input Rock(r), Paper(p), or Scissors(s)? \n> ").lower()

        while(userinput != "r" and userinput != "p" and userinput != "s"):
            print("Input must be 'r', 'p', or 's'.")
            userinput = input("P1: Rock(r), Paper(p), or Scissors(s)? \n> ").lower()

        otherinput = player_two_chooses(playertype)

        if(userinput == otherinput):
            print("Tie") 
            ties = ties + 1
            logger.log("[RPS] Tied outcome!")

        elif((userinput == "p" and otherinput == "s") or
        (userinput == "s" and otherinput == "r") or
        (userinput == "r" and otherinput == "p")):
            print("P2 Wins (" + otherinput + " beats " + userinput + ")")
            p_two_score = p_two_score + 1
            logger.log("[RPS] P2 Wins (" + otherinput + " beats " + userinput + ")")

        else:
            print("P1 Wins (" + userinput + " beats " + otherinput+ ")")
            p_one_score = p_one_score + 1
            logger.log("[RPS] P1 Wins (" + userinput + " beats " + otherinput+ ")")

        totalloop = input("Do you want to play again? y/n \n> ").lower()

        while (totalloop != "y" and totalloop != "n"):
            totalloop = input("Input must be 'y' or 'n'. \n> ").lower()

    end_time = time.time()
    logger.log("[RPS] User spent " + logger.time_format(end_time - start_time) + " playing Rock Paper Scissors with "
               + str(p_one_score) + " points to P1, " + str(p_two_score) + " points to P2, and " + str(ties) + " ties!")