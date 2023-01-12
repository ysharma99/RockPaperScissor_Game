import random

def play():
    user = input("Make your choice! r for rock, p for paper, s for scissor! ")
    computer = random.choice(['r','p','s'])

    choice = (['r','p','s'])
    if choice!= user:
        print("Oops that's not one of the choices! its r for rock, p for paper, s for scissor")

    if user == computer:
        return 'It\'s a tie' #returns this function

    # r > s, s> p, p>r 
    #user is the player, opponenet is the computer
    if winner(user,computer):
        return 'You won! :) '  #returns to function
    
    return 'You lost :( ' #only way to get to this line is if the other ones are not true



def winner(player, opponent):
    #return true if the player wins 
    # r > s, s> p, p>r 
    if (player =='r') and (opponent =='s') or (player=='s') and (opponent=='p') or (player=='p') and (opponent=='r'):
        return True 

print (play())



