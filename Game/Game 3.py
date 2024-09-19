import random

def display_intro():
    print("Welcome to the Mystic Forest Adventure!")
    print("You find yourself at the edge of a mysterious forest.")
    print("Your goal is to find the hidden treasure.")
    print("Be careful of the dangers that lurk in the shadows!\n")

def make_choice(options):
    while True:
        choice = input("Enter your choice (1-" + str(len(options)) + "): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("Invalid choice. Please try again.")

def forest_path():
    print("\nYou're on a narrow path in the forest.")
    print("1. Go deeper into the forest")
    print("2. Climb a nearby tree")
    print("3. Rest for a while")
    
    choice = make_choice([1, 2, 3])
    
    if choice == 1:
        print("\nYou venture deeper into the forest...")
        return "deep_forest"
    elif choice == 2:
        print("\nYou climb the tree and spot a shimmering light in the distance!")
        return "tree_top"
    else:
        print("\nYou rest for a while and feel refreshed.")
        return "forest_path"

def deep_forest():
    print("\nYou're in a dark part of the forest.")
    print("1. Search for clues")
    print("2. Call out for help")
    print("3. Turn back")
    
    choice = make_choice([1, 2, 3])
    
    if choice == 1:
        if random.random() < 0.5:
            print("\nYou found a map fragment!")
        else:
            print("\nYou found nothing of interest.")
        return "deep_forest"
    elif choice == 2:
        print("\nYour call echoes through the forest, but no one responds.")
        return "deep_forest"
    else:
        print("\nYou decide to head back.")
        return "forest_path"

def tree_top():
    print("\nFrom the tree top, you see a cave and a river.")
    print("1. Climb down and head towards the cave")
    print("2. Climb down and go to the river")
    print("3. Stay in the tree and observe")
    
    choice = make_choice([1, 2, 3])
    
    if choice == 1:
        print("\nYou make your way to the cave...")
        return "cave"
    elif choice == 2:
        print("\nYou head towards the river...")
        return "river"
    else:
        print("\nYou observe the surroundings but see nothing new.")
        return "tree_top"

def cave():
    print("\nYou're at the entrance of a dark cave.")
    print("1. Enter the cave")
    print("2. Search around the entrance")
    print("3. Leave the cave")
    
    choice = make_choice([1, 2, 3])
    
    if choice == 1:
        if random.random() < 0.3:
            print("\nCongratulations! You found the hidden treasure in the cave!")
            return "end"
        else:
            print("\nYou explore the cave but find nothing. It's getting dark.")
            return "cave"
    elif choice == 2:
        print("\nYou find some interesting rocks, but no treasure.")
        return "cave"
    else:
        print("\nYou decide to leave the cave area.")
        return "forest_path"

def river():
    print("\nYou're by a fast-flowing river.")
    print("1. Try to cross the river")
    print("2. Follow the river downstream")
    print("3. Go back to the forest")
    
    choice = make_choice([1, 2, 3])
    
    if choice == 1:
        if random.random() < 0.4:
            print("\nYou successfully cross the river and find the treasure on the other side!")
            return "end"
        else:
            print("\nThe current is too strong. You return to the riverbank.")
            return "river"
    elif choice == 2:
        print("\nYou follow the river but it leads you in circles.")
        return "forest_path"
    else:
        print("\nYou head back into the forest.")
        return "forest_path"

def play_game():
    display_intro()
    location = "forest_path"
    
    while location != "end":
        if location == "forest_path":
            location = forest_path()
        elif location == "deep_forest":
            location = deep_forest()
        elif location == "tree_top":
            location = tree_top()
        elif location == "cave":
            location = cave()
        elif location == "river":
            location = river()
    
    print("\nCongratulations! You've completed the Mystic Forest Adventure!")
    print("Thanks for playing!")

# Start the game
play_game()