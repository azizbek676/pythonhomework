import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

def play_game():
    player_score = 0
    computer_score = 0
    while player_score < 5 and computer_score < 5:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")
        
        print(f"Score - Player: {player_score}, Computer: {computer_score}")
    
    if player_score == 5:
        print("Congratulations! You won the match!")
    else:
        print("Computer won the match. Better luck next time!")

if __name__ == "__main__":
    play_game()