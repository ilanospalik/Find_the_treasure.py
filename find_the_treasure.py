import random

def create_treasure_file():
    treasure_data = ""
    
    # Generate random number of occurrences for each digit
    for i in range(10):
        count = random.randint(1, 20)
        treasure_data += str(i) * count
    
    treasure_data += "TREASURE"
    
    # Append digits in descending order
    for i in range(9, -1, -1):
        count = random.randint(1, 20)
        treasure_data += str(i) * count
    
    with open("treasure.txt", "w") as file:
        file.write(treasure_data)

def search_treasure():
    with open("treasure.txt", "r") as file:
        treasure_data = file.read()
    
    found_treasure = False
    num_moves = 0
    
    while not found_treasure:
        print("Where do you want to move? [1 - forward, 2 - back]")
        direction = int(input())
        
        print("How many steps?")
        num_characters = int(input())
        
        if direction == 1:
            new_position = num_moves + num_characters
        elif direction == 2:
            new_position = num_moves - num_characters
        else:
            print("Invalid direction! Please choose 1 or 2.")
            continue
        
        if new_position < 0 or new_position >= len(treasure_data):
            print("You reached the end.the Game ended!")
            break
        
        moved_character = treasure_data[new_position]
        print(f"You landed on: {moved_character}")
        
        if moved_character == "T":
            found_treasure = True
        
        num_moves += num_characters
    
    print(f"Congratulations! You found the treasure in {num_moves} moves.")

# Step One - Create treasure file
create_treasure_file()

# Step Two - Search for the treasure
search_treasure()
