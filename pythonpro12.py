def player_turn(current_number):
    while True:
        try:
            choice = int(input("Choose to add 1, 2, or 3 to the current number: "))
            if choice in [1, 2, 3]:
                return current_number + choice
            else:
                print("Invalid choice,")
        except ValueError:
            print("Please enter .")

def computer_turn(current_number):
    
    choice = (4 - (current_number % 4)) if current_number % 4 != 0 else 1
    print(f"Computer chooses to add {choice}.")
    return current_number + choice

def number_21_game():
    current_number = 0
    print("Welcome  avoid saying 21.")
    
    while current_number < 21:
   
        current_number = player_turn(current_number)
        print(f"Curr: {current_number}")
        if current_number >= 21:
            print("You lose! You said 21.")
            break
        
     
        current_number = computer_turn(current_number)
        print(f"Currer: {current_number}")
        if current_number >= 21:
            print("Compu! You win!")
            break


if __name__ == "__main__":
    number_21_game()
import random

def roll_dice():
    return random.randint(1, 6)

def dice_roll_simulator():
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")
        
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    dice_roll_simulator()
