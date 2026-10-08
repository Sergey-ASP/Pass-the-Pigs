import random
import sys

class Player():
    def __init__(self, player_number):
        self._saved_points = 0
        self._player_number = player_number
        self._round_points = 0

    def decide_roll(self) -> bool:
        '''Decides whether to roll the pigs or stop and returns it as a boolean value.'''
        pass

    def bank_points(self):
        self._saved_points += self._round_points
        self._round_points = 0

    def gain_points(self, points):
        self._round_points += points

    def get_player_number(self):
        return self._player_number

    def get_total_points(self):
        return self._saved_points + self._round_points

    def pig_out(self):
        self._round_points = 0

class UserPlayer(Player):
    def __init__(self, player_number):
        super().__init__(player_number)

    def decide_roll(self):
        # ask the user if they should roll or not
        print(f'You have {self._saved_points} points saved, and {self._round_points} additional points this round.')
        while True:
            selection = input('Would you like to roll the pigs?  Enter either "yes" or "no". ')
            match selection:
                case 'yes':
                    return True
                case 'no':
                    return False
                case _:
                    print(f'"{selection}" is not a valid input.')


class RandomPlayer(Player):
    def __init__(self, player_number):
        super().__init__(player_number)

    def decide_roll(self):
        if self._round_points == 0:
            return True
        else:
            return random.randint(0,1) == 1

class GamblePlayer(Player):
    def __init__(self, player_number):
        super().__init__(player_number)

    def decide_roll(self):
        return True

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

    point_amounts = {
        'Sider': 0,
        'Razorback': 5,
        'Trotter': 5,
        'Snouter': 10,
        'Leaning Jowler': 15
    }

    print('Welcome to the pass the pigs game!')

    players = []

    # make sure player was specified
    if len(sys.argv) < 2:
        print('you need to specify at least one player!  use either random, user, or gamble.')
        sys.exit(-1)

    # using command line arguments, populate the playerlist
    for i, player in enumerate(sys.argv[1:]):
        if player.lower() == 'random': # randomplayer
            players.append(RandomPlayer(i+1))
        elif player.lower() == 'user': #userplayer
            players.append(UserPlayer(i+1))
        elif player.lower() == 'gamble': #userplayer
            players.append(GamblePlayer(i+1))

    # Loop over each player until someone wins
    while True:
        for current_player in players:
            current_player: Player
            p_num = current_player.get_player_number()
            print(f'It\'s player {p_num}\'s turn!')

            # While the player wants to keep rolling their pigs:
            while current_player.decide_roll():
                # roll pigs
                pig1 = get_pig_state(random.randint(0,1000))
                pig2 = get_pig_state(random.randint(0,1000))

                # calculate how many points the player should get
                points = point_amounts[pig1] + point_amounts[pig2]

                # if player rolled doubles, double the points they got.
                if pig2 == pig1:
                    points *= 2

                    # if player rolled two siders, flip coin to see if they pig out.
                    # otherwise, they get one point for a sider.
                    if points == 0:
                        if random.randint(0,1) == 0:
                            print ('Pig out!  You lost all points for this round.')
                            current_player.pig_out()
                            break
                        else:
                            points = 1

                # print the points back to the user and update the number of points they gained this round
                print(f'Player {p_num} rolled a {pig1} and a {pig2}, earning them {points} points.')
                current_player.gain_points(points)

                # player wins the game if they have 100 points
                if current_player.get_total_points() >= 100:
                    print(f'Player {p_num} won the game with {current_player.get_total_points()} points.')
                    return

            # once player stops rolling, bank points they have saved up.
            current_player.bank_points()
            print(f'Player {p_num} now has {current_player.get_total_points()} points.')

main()