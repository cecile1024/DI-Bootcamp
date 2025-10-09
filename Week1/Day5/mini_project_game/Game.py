# this will contain a Game class which will have functions to play a single game 
# of rock-paper-scissors against the computer, determine the game’s result, and return the result.
import random
class Game():
    def __init__(self):
        pass
#  – Ask the user to select an item (rock/paper/scissors). 
# Keep asking until the user has selected one of the items – use data validation and looping. 
# Return the item at the end of the function.
    def get_user_item(self):
        user_item=None
        while user_item not in ("r", "p", "s"):
            user_item=input("Select (r)ock, (p)aper, or (s)cissors :")
            # print(f"You chose :{user_item}")
        return user_item
# get_computer_item(self) – Select rock/paper/scissors at random for the computer. 
# Return the item at the end of the function. Use python’s random.choice() function (read about it online).
    def get_computer_item(self):
        computer_item=random.choice(["r", "p", "s"])
        # print(f"Computer chose :{computer_item}")
        return computer_item
# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# Return either the user win, draw, or loss.
    def get_game_result(self, user_item, computer_item):
        # Cas d'égalité
        if user_item == computer_item:
            result="draw"
            # print(result)
            return result
        # Cas où le user gagne
        elif (user_item == "r" and computer_item == "s") or \
            (user_item == "s" and computer_item == "p") or \
            (user_item == "p" and computer_item == "r"):
            result= "win"
            print(result)
            return result
        else:
            result="loss"
            print(result)
            return result
# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). 
# Get the user’s item (rock/paper/scissors) and remember it
# Get a random item for the computer (rock/paper/scissors) and remember it
# Determine the results of the game# Print the output of the game; 
    def play(self):
        user_item=self.get_user_item()
        computer_item=self.get_computer_item()
        result=self.get_game_result(user_item,computer_item)
        print(f"You selected {user_item}, the computer selected {computer_item} : you {result}")
        return result


# tests/ a retirer pour former le module à importer
# newgame=Game()
# newgame.get_user_item()
# newgame.get_computer_item()
# newgame.get_game_result(newgame.get_user_item,newgame.get_computer_item)
# newgame.play()