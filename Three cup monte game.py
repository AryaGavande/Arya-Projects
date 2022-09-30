#Three cup monte - a simple game which involve randomn guessing of item hidden in one of the cup. The players are tricked by shuffling the cups.

from random import shuffle


cups = [' ','O',' ']   #(the capital o reprsents the element that players need to guess)  

def player_guess():
    guess = 'O'
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1 or 2")
    return int(guess)

def check_guess(cups,guess):
    if guess == '':
        print("Correct")
    else:
        print("Wrong guess!")
        print(cups)

#INTIAL LIST

#SHUFFLED LIST
mixed_up = shuffle(cups)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixed_up,guess)   