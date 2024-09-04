import random

def display_intro():
    print("Welcome to the Dungeon Adventure!")
    print("You are in a dark dungeon. There are two doors: one to the left and one to the right.")
    print("Your goal is to find the treasure hidden in the dungeon.\n")

def choose_door():
    while True:
        choice = input("Which door do you choose? (left/right): ").strip().lower()
        if choice in ["left", "right"]:
            return choice
        print("Invalid choice. Please type 'left' or 'right'.")

def encounter():
    outcomes = [
        "You find a treasure chest filled with gold!",
        "You are attacked by a dragon and lose half your health!",
        "You find a magical potion that restores your health!",
        "You encounter a friendly wizard who offers you advice."
    ]
    return random.choice(outcomes)

def play_game():
    display_intro()
    
    player_health = 100
    treasures_found = 0

    while True:
        door = choose_door()
        print(f"\nYou chose the {door} door.")
        
        event = encounter()
        print(event)
        
        if "treasure" in event:
            treasures_found += 1
            print(f"You have found {treasures_found} treasure(s) so far.")
        elif "dragon" in event:
            player_health -= 50
            if player_health <= 0:
                print("You have been defeated by the dragon. Game over!")
                break
            else:
                print(f"Your current health is {player_health}.")
        elif "potion" in event:
            player_health = min(100, player_health + 30)
            print(f"Your current health is {player_health}.")
        elif "wizard" in event:
            print("The wizard advises you to choose wisely and explore thoroughly.")

        if treasures_found >= 3:
            print("\nCongratulations! You have found all the treasures and completed the adventure!")
            break

        if input("\nDo you want to continue exploring? (yes/no): ").strip().lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
