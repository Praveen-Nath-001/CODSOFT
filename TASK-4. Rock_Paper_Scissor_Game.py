import random

def stone_paper_scissor(user_choice, user_score, comp_score):
    choices = ['stone', 'paper', 'scissor']
    comp_choice = random.choice(choices)
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {comp_choice}")

    if user_choice == comp_choice:
        print("Result: The match is drawn")
    elif (user_choice == 'stone' and comp_choice == 'scissor') or \
         (user_choice == 'paper' and comp_choice == 'stone') or \
         (user_choice == 'scissor' and comp_choice == 'paper'):
        print("Result: User wins the match")
        user_score += 1
    else:
        print("Result: Computer wins the match")
        comp_score += 1

    print(f"Scores => User: {user_score}, Computer: {comp_score}")
    return user_score, comp_score

def main():
    user_score = 0
    comp_score = 0
    choices = ['stone', 'paper', 'scissor']

    while True:
        user_input = input("Enter your choice (stone/paper/scissor): ").lower()
        if user_input not in choices:
            print("Invalid input. Please choose stone, paper, or scissor.")
            continue

        user_score, comp_score = stone_paper_scissor(user_input, user_score, comp_score)

        cont = input("Do you want to play again? (yes/no): ").lower()
        if cont == 'no':
            print("\nFinal Result:")
            if user_score > comp_score:
                print("🎉 User wins the game!")
            elif comp_score > user_score:
                print("💻 Computer wins the game!")
            else:
                print("🤝 The game is drawn.")
            print("Thanks for playing!")
            break
        elif cont != 'yes':
            print("Invalid input. Exiting game.")
            break

if __name__ == "__main__":
    main()
