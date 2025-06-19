import random
import time

# ASCII Art for Rock, Paper, Scissors
ascii_art = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    "paper": '''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}

def print_welcome():
    print("╔═══════════════════════════════════════════╗")
    print("║        🎮 ROCK, PAPER, SCISSORS BATTLE!     ║")
    print("╚═══════════════════════════════════════════╝")
    print("💡 First to 5 wins takes the match!")
    print("🎯 Choose rock, paper or scissors each round.\n")

def get_user_choice():
    choice = input("👉 Your move (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("❌ Invalid choice. Try again.")
        choice = input("👉 Your move (rock/paper/scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def print_choices(user_choice, computer_choice):
    print("\n🧑 You chose:")
    print(ascii_art[user_choice])
    time.sleep(1)
    print("🤖 Computer chose:")
    print(ascii_art[computer_choice])

def show_score(user_score, comp_score, ties):
    print("╔══════════════════════╗")
    print(f"  👤 YOU: {user_score}  |  🤖 COMPUTER: {comp_score}  |  🤝 TIES: {ties}")
    print("╚══════════════════════╝\n")

def play_game():
    print_welcome()
    user_score = 0
    comp_score = 0
    ties = 0

    while user_score < 5 and comp_score < 5:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()

        print_choices(user_choice, comp_choice)
        winner = determine_winner(user_choice, comp_choice)

        if winner == "tie":
            print("🤝 It's a TIE!\n")
            ties += 1
        elif winner == "user":
            print("🎉 You WIN this round!\n")
            user_score += 1
        else:
            print("💻 Computer WINS this round!\n")
            comp_score += 1

        show_score(user_score, comp_score, ties)
        time.sleep(1)

    # Final result
    print("🎮 MATCH OVER!")
    if user_score > comp_score:
        print("🏆 CONGRATULATIONS! You beat the computer!\n")
    else:
        print("💔 The computer wins. Better luck next time!\n")

# Start the game
play_game()
