import os
import random

# Function to clear the console (for better game experience)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_map():
    """Generates a 5x5 game map with randomly placed Player (P), Key (K), and Door (D)."""
    # Initialize an empty 5x5 grid
    game_map = [[' ' for _ in range(5)] for _ in range(5)]

    # Randomly place Player (P), Key (K), and Door (D) on the map
    positions = random.sample(range(25), 3)  # Get 3 unique random positions (0 to 24)
    player_pos = divmod(positions[0], 5)  # Convert flat index to (row, col)
    key_pos = divmod(positions[1], 5)
    door_pos = divmod(positions[2], 5)

    # Place Player (P), Key (K), and Door (D) on the map
    game_map[player_pos[0]][player_pos[1]] = 'P'
    game_map[key_pos[0]][key_pos[1]] = 'K'
    game_map[door_pos[0]][door_pos[1]] = 'D'

    return game_map, player_pos

def print_map(game_map):
    """Prints the current state of the game map."""
    clear_console()
    for row in game_map:
        print(' '.join(row))
    print("\nControls: W (Up), S (Down), A (Left), D (Right)")
    print("Objective: Collect the key (K) and reach the door (D) to escape.")

def move_player(direction, game_map, player_pos):
    """Moves the player based on the input direction."""
    global key_collected
    
    # Calculate new position
    new_row, new_col = player_pos
    if direction == 'W':
        new_row -= 1  # Move up
    elif direction == 'S':
        new_row += 1  # Move down
    elif direction == 'A':
        new_col -= 1  # Move left
    elif direction == 'D':
        new_col += 1  # Move right

    # Check boundaries
    if new_row < 0 or new_row >= len(game_map) or new_col < 0 or new_col >= len(game_map[0]):
        print("Cannot move outside the map!")
        return player_pos  # Return the old position if out of bounds
    
    # Check what's in the new position
    next_pos = game_map[new_row][new_col]
    
    if next_pos == 'K':
        # Collect the key
        key_collected = True
        print("You collected the key!")
    
    elif next_pos == 'D':
        # Check if the player has collected the key
        if key_collected:
            print("Congratulations! You unlocked the door and escaped!")
            return None  # End the game
        else:
            print("You reached the door but don't have the key! Game Over.")
            return None  # End the game
    
    # Update map
    game_map[player_pos[0]][player_pos[1]] = ' '  # Clear the old position
    game_map[new_row][new_col] = 'P'  # Move to the new position
    return [new_row, new_col]  # Update player's position

def main():
    """Main function to run the game loop."""
    global key_collected

    while True:
        key_collected = False  # Reset key status for new game
        
        # Generate a random game map and player position
        game_map, player_pos = generate_random_map()
        
        print_map(game_map)
        
        # Game loop
        while player_pos:
            # Get the player's move
            move = input("\nEnter your move (W/A/S/D): ").upper()
            if move in ['W', 'A', 'S', 'D']:
                player_pos = move_player(move, game_map, player_pos)
                print_map(game_map)
            else:
                print("Invalid input! Please enter W, A, S, or D.")

        # Ask the player if they want to play again
        new_game = input("Do you want to start a new game? (yes or no): ").strip().lower()
        if new_game != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
