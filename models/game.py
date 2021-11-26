
class Game:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def determine_winner(player_1, player_2):
        if player_1 == 'rock' and player_2 == 'rock':
            return "It's a Draw! - Go again!"
        elif player_1 == 'paper' and player_2 =='paper':
            return "It's a Draw! - Go again!"
        elif player_1 == 'scissors' and player_2 =='scissors':
            return "It's a Draw! - Go again!"
        elif player_1 == 'rock' and player_2 =='paper':
            return "Player 2 Wins! - Go again!"
        elif player_1 == 'paper' and player_2 =='scissors':
            return "Player 2 Wins! - Go again!"
        elif player_1 == 'scissors' and player_2 =='rock':
            return "Player 2 Wins! - Go again!"
        elif player_1 == 'paper' and player_2 =='rock':
            return "Player 1 Wins! - Go again!"
        elif player_1 == 'scissors' and player_2 =='paper':
            return "Player 1 Wins! - Go again!"
        elif player_1 == 'rock' and player_2 =='scissors':
            return "Player 1 Wins! - Go again!"
        else:
            return None