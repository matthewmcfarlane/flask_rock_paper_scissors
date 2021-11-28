
class Game:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def determine_winner(player_1, player_2):
        if player_1 == 'rock' and player_2 == 'rock':
            return "You both chose rock! - Go again"
        elif player_1 == 'paper' and player_2 =='paper':
            return "You both chose paper! - Go again"
        elif player_1 == 'scissors' and player_2 =='scissors':
            return "You both chose scissors! - Go again"
        elif player_1 == 'rock' and player_2 =='paper':
            return f"Player 1 chose {player_1} and the player 2 chose {player_2}, Player 2 wins - Go again!"
        elif player_1 == 'paper' and player_2 =='scissors':
            return f"Player 1 chose {player_1} and the player 2 chose {player_2}, Player 2 wins - Go again!"
        elif player_1 == 'scissors' and player_2 =='rock':
            return f"Player 1 chose {player_1} and the player 2 chose {player_2}, Player 2 wins - Go again!"
        elif player_1 == 'paper' and player_2 =='rock':
            return f"Player 1 chose {player_1} and the player 2 chose {player_2}, Player 1 wins - Go again!"
        elif player_1 == 'scissors' and player_2 =='paper':
            return f"Player 1 chose {player_1} and the player 2 chose {player_2}, Player 1 wins - Go again!"
        elif player_1 == 'rock' and player_2 =='scissors':
            return f"Player 1 chose {player_1} and the player 2 chose {player_2}, Player 1 wins - Go again!"
        else:
            return None

    def determine_winner_cpu(player_1, cpu):
        if player_1 == 'rock' and cpu == 'rock':
            return "You both chose rock!"
        elif player_1 == 'paper' and cpu =='paper':
            return "You both chose paper!"
        elif player_1 == 'scissors' and cpu =='scissors':
            return "You both chose scissors!"
        elif player_1 == 'rock' and cpu =='paper':
            return f"You chose {player_1} and the computer chose {cpu} -  Computer Wins!"
        elif player_1 == 'paper' and cpu =='scissors':
            return f"You chose {player_1} and the computer chose {cpu} -  Computer Wins!"
        elif player_1 == 'scissors' and cpu =='rock':
            return f"You chose {player_1} and the computer chose {cpu} -  Computer Wins!"
        elif player_1 == 'paper' and cpu =='rock':
            return f"You chose {player_1} and the computer chose {cpu} -  You Win!"
        elif player_1 == 'scissors' and cpu =='paper':
            return f"You chose {player_1} and the computer chose {cpu} -  You Win!"
        elif player_1 == 'rock' and cpu =='scissors':
            return f"You chose {player_1} and the computer chose {cpu} -  You Win!"
        else:
            return None