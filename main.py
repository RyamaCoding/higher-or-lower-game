import art
import random 
import game_data
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_comparison(choiceA, choiceB, first_correct_answer, score=None):
    print(art.logo)
    if first_correct_answer and score is not None:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {choiceA.get('name')}, a {choiceA.get('description')}, from {choiceA.get('country')}")
    print(art.vs)
    print(f"Against B: {choiceB.get('name')}, a {choiceB.get('description')}, from {choiceB.get('country')}")   

# Main game function
def game():
    score = 0
    game_over = False
    first_correct_answer = False

    choiceA = random.choice(game_data.data)
    choiceB = random.choice(game_data.data)

    # Ensure choiceA and choiceB are not the same initially
    while choiceA == choiceB:
        choiceB = random.choice(game_data.data)

    # Display the initial comparison (without score)
    game_comparison(choiceA, choiceB, first_correct_answer)

    while not game_over:
    
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_choice == 'A':
            if choiceA.get('follower_count') > choiceB.get('follower_count'):
                score += 1
                first_correct_answer = True
                # Update choiceB with a new random choice
                choiceB = random.choice(game_data.data)
                while choiceA == choiceB:
                    choiceB = random.choice(game_data.data)
            else: 
                print(f"Sorry, that's wrong! Final score: {score}")
                game_over = True
        
        elif user_choice == 'B':
            if choiceB.get('follower_count') > choiceA.get('follower_count'):
                score += 1
                first_correct_answer = True
                # Set choiceA to the winner (choiceB becomes new choiceA)
                choiceA = choiceB
                choiceB = random.choice(game_data.data)
                while choiceA == choiceB:
                    choiceB = random.choice(game_data.data)
            else:
                print(f"Sorry, that's wrong! Final score: {score}")
                game_over = True

        else: 
            print("Invalid input. Please try again.")

        # If the game is still ongoing, clear the screen and display updated comparison
        if not game_over:
            clear_screen()
            # Always display the score after the first correct answer
            game_comparison(choiceA, choiceB, first_correct_answer, score)

# Run the game
game()