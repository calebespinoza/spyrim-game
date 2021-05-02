from spyrim_map import SpyrimMap
import random

x_border = 15
y_border = 25
x = random.randint(0, x_border - 1)
y = random.randint(0, y_border - 1)

spyrimmap = SpyrimMap(x_border, y_border)
the_map = spyrimmap.create_map()

def get_position(x, y, the_map):
    for row in range(len(the_map)):
        if row == y:
            for col in range(len(the_map[row])):
                if col == x:
                    return the_map[row][col]
#print(f"x = {x}")
#print(f"y = {y}")
print(f"You are in {get_position(x, y, the_map)}")
run = True
while run:
    opt = input("command: ")
    if opt == 'exit':
        run = False
        print("Bye!")
    else:
        if opt == "go north":
            if get_position(x, y - 1, the_map) != None:
                y -= 1
            else:
                print("You've gotten at the edge north of the map.")
        if opt == "go south":
            if get_position(x, y + 1, the_map) != None:
                y += 1
            else:
                print("You've gotten at the edge south of the map.")
        if opt == "go west":
            if get_position(x - 1, y, the_map) != None:
                x -= 1
            else:
                print("You've gotten at the edge west of the map.")
        if opt == "go east":
            if get_position(x + 1, y, the_map) != None:
                x += 1
            else:
                print("You've gotten at the edge west of the map.")
        
        print(f"You are in {get_position(x, y, the_map)}")
        