#from spyrim_map import SpyrimMap
from beginner_map import BegineerMap
from expert_map import ExpertMap
from pro_map import ProMap
import random
import argparse
import sys

# Level Arguments

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--level", dest="level", default="beginner", type=str, help="choose a level to start the game: beginner, expert, pro")

args = parser.parse_args()
level = str(args.level)

game_map = None

if level == "beginner":
    game_map = BegineerMap(15, 15)
    game_map.create_map()
    game_map.print_map(game_map.map)
elif level == "expert":
    game_map = ExpertMap(20, 20)
    game_map.create_map()
    game_map.print_map(game_map.map)
elif level == "pro":
    game_map = ProMap(30, 30)
    game_map.create_map()
    game_map.print_map(game_map.map)
else:
    print("Unknown level.") 
    print("Get help with -h or --help.")
    sys.exit(1)

print(f"You have chosen '{level}' level.")
print("Write 'help' to review the allowed commands.")

x = random.randint(0, game_map.y - 1)
y = random.randint(0, game_map.x - 1)
#print(f"{y}-{x}")

def get_position(x, y, the_map):
    for row in range(len(the_map)):
        if row == y:
            for col in range(len(the_map[row])):
                if col == x:
                    return the_map[row][col]

#print(f"You are in {get_position(x, y, game_map.map)}")
run = True
while run:
    opt = input("command: ")
    if opt == 'exit':
        run = False
        print("Bye!")
    elif opt == "help":
        print("'go north' - Move a position to the north.")
        print("'go south' - Move a position to the south.")
        print("'go west' - Move a position to the west.")
        print("'go east' - Move a position to the east.")
    else:
        if opt == "go north":
            if get_position(x, y - 1, game_map.map) != None:
                y -= 1
            else:
                print("You've gotten at the edge north of the map.")
        if opt == "go south":
            if get_position(x, y + 1, game_map.map) != None:
                y += 1
            else:
                print("You've gotten at the edge south of the map.")
        if opt == "go west":
            if get_position(x - 1, y, game_map.map) != None:
                x -= 1
            else:
                print("You've gotten at the edge west of the map.")
        if opt == "go east":
            if get_position(x + 1, y, game_map.map) != None:
                x += 1
            else:
                print("You've gotten at the edge west of the map.")
        
        print(f"You are in {get_position(x, y, game_map.map)}")
        