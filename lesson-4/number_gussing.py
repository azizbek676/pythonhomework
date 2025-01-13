import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Enter your guess (between 1 and 100): "))
        
        if guess > number_to_guess:
            print("Too high!")
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("You guessed it right!")
            return
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    
    print("You lost. Want to play again?")
    play_again = input("Type 'Y', 'YES', 'y', 'yes', 'ok' to play again: ")
    if play_again in ['Y', 'YES', 'y', 'yes', 'ok']:
        play_game()

if __name__ == "__main__":
    play_game()