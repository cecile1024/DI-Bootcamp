# his will contain functions to show the main menu, handle user’s input, 
# and show the game summary before exiting.

# get_user_menu_choice() - this should display a simple menu, 
# get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit
from Game import Game

def get_user_menu_choice():
    print("Menu :\n"
    "     (g) Play a new game \n" 
    "     (x) Show scores and exit\n"
    "     (q) Quit the game")
    user_choice=None
    while user_choice not in ("g","x","q"):
           user_choice=input("Enter your choice:")
           print(f":{user_choice}")
    return user_choice


# print_results(results) # results={'win': 2,'loss': 4,'draw': 3}
# Bear in mind that this dictionary will need to be created and populated in some other part of our code, 
# and passed in to the print_results function at the right time.
def print_results(results):
    print("Game results:")
    print("  You won {} times".format(results['win']))
    print("  You lost {} times".format(results['loss']))
    print("  You drew {} times".format(results['draw']))
    print("\nThank you for playing!\n")

# main() - the main function. It should take care of 3 things:
# Displaying the menu repeatedly, until the user types in the value to exit the program: 
# ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)
# When the user chooses to play a game:# Create a new Game object (see below), 
# and call its play() function, receiving the result of the game that is returned.
# Remember the results of every game that is played.
# When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.

def main():
     results={'win':0,'loss':0, 'draw':0} #initialise result
     user_choice=get_user_menu_choice()
     while user_choice is 'g':
        newgame=Game()
        result=newgame.play()
        results[result]+=1
        user_choice=get_user_menu_choice() #display menu
     
     if user_choice=='x':
        print_results(results)
     elif user_choice=='q':
        return
     
main()