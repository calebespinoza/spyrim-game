
from beginner_map import BegineerMap
from expert_map import ExpertMap
from pro_map import ProMap
from avatar import Avatar
from game_core import GameCore
import random
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--level", dest="level", default="beginner", type=str, help="choose a level to start the game: beginner, expert, pro")

args = parser.parse_args()
level = str(args.level)

game_map = None
if level == "beginner":
    game_map = BegineerMap(15, 15)
elif level == "expert":
    game_map = ExpertMap(20, 20)
elif level == "pro":
    game_map = ProMap(30, 30)
else:
    print("Unknown level.") 
    print("Get help with -h or --help.")
    sys.exit(1)

game_core = GameCore()
game_map.create_map()
avatar = Avatar(random.randint(0, game_map.y - 1), random.randint(0, game_map.x - 1))

#game_map.print_map(game_map.map)

print("======================================================================")
print("                           Game Storie")
print("======================================================================")
print("We are in the mid-earth age, the world is populated by humans, elves, ")
print("giants, argonians and khajiits. People live in small towns and villa- ")
print("ges, dedicating to farming, cattling, and commerce. These are hard ti-")
print("mes, there are droughts in summer and quite a lot of snow in winter,  ")
print("but the biggest threaten are dragons. They destroy towns and kill men,")
print("women and children and they burning everything as well, houses, farms,")
print("animals, so on. Nobody has been able to confront and kill them.       ")
print("Legends say that only a human 'The Dovakin' might kill all of them and")
print("protect the world from them. You're the human who can kill the dragons")
print("Show the people that that the legends are true. Show them that you are")
print("their 'Dovakin'.")
print("======================================================================")

print(f"You have chosen '{level}' level.")
print("Write 'help' to review the allowed commands.")
print(f"Current Position: Your are in {game_core.get_position(avatar.x_position, avatar.y_position, game_map.map)} |{avatar.y_position},{avatar.x_position}|")
#sys.exit(1)

run = True
while run:
    opt = input("Command: ")
    if opt == 'exit':
        run = False
        print("Bye!")
    elif opt == "help":
        print("'go north' or 'gn' - Move a position to the north.")
        print("'go south' or 'gs' - Move a position to the south.")
        print("'go west' or 'gw' - Move a position to the west.")
        print("'go east' or 'ge' - Move a position to the east.")
        print("'kill dragon' or 'kd' - Kill a dragon if you find any.")
        print("'exit' - Quit the game.")
    else:
        game_core.command_exec(avatar, game_map.map, opt)