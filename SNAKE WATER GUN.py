import random

# Mapping for user input and corresponding values
you_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

# Computer's random choice
computer = random.choice([1, -1, 0])

# Taking input from the user
you_str = input("Enter 's' for Snake, 'w' for Water, or 'g' for Gun: ").lower()

# Validating user input
if you_str not in you_dict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    # Getting user choice
    you = you_dict[you_str]
    
    # Displaying choices
    print(f"You chose: {reverse_dict[you]}")
    print(f"Computer chose: {reverse_dict[computer]}")
    
    # Determining the outcome
    if computer == you:
        print("It's a draw!")
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print("You lose!")
    else:
        print("You win!")
