import random
import sys

class Player():
    # TODO
    
    pass

def get_pig_state(pig_value):
    '''returns the state of the pig given roll value.
    
    Args:
        pig_value (int): Pig roll value between 0 and 1000'''

    if pig_value < 651:
        return 'Sider'
    elif pig_value < 875:
        return 'Razorback'
    elif pig_value < 963:
        return 'Trotter'
    elif pig_value < 993:
        return 'Snouter'
    else:
        return 'Leaning Jowler'

def main():
    '''Runs pass the pigs'''

    point_amounts = { # dictionary containing point amounts for each pig state
        'Sider': 0,
        'Razorback': 5,
        'Trotter': 5,
        'Snouter': 10,
        'Leaning Jowler': 15
    }

    # TODO

main()