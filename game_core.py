class GameCore(object):
    def __init__(sefl):
        pass


    def get_position(self, x, y, the_map):
        for row in range(len(the_map)):
            if row == y:
                for col in range(len(the_map[row])):
                    if col == x:
                        return the_map[row][col]
    
    def command_exec(self, avatar, game_map, command):
        if command == "go north" or command == "gn":
            self.go_north(avatar, game_map)
        elif command == "go south" or command == "gs":
            self.go_south(avatar, game_map)
        elif command == "go west" or command == "gw":
            self.go_west(avatar, game_map)
        elif command == "go east" or command == "ge":
            self.go_east(avatar, game_map)
        elif command == "kill dragon" or command == "kd":
            self.kill_dragon(avatar, game_map)
        else:
            raise ValueError(f"Command '{command}' unknown.")

        self.print_messages(avatar, game_map)
    
    def go_north(self, avatar, game_map):
        if self.get_position(avatar.x_position, avatar.y_position - 1, game_map) != None:
            avatar.y_position -= 1
        else:
            print("Warning: You've gotten at the edge north of the map.")
    
    def go_south(self, avatar, game_map):
        if self.get_position(avatar.x_position, avatar.y_position + 1, game_map) != None:
            avatar.y_position += 1
        else:
            print("You've gotten at the edge south of the map.")

    def go_west(self, avatar, game_map):
        if self.get_position(avatar.x_position - 1, avatar.y_position, game_map) != None:
            avatar.x_position -= 1
        else:
            print("You've gotten at the edge west of the map.")

    def go_east(self, avatar, game_map):
        if self.get_position(avatar.x_position + 1, avatar.y_position, game_map) != None:
            avatar.x_position += 1
        else:
            print("You've gotten at the edge west of the map.")
    
    def kill_dragon(self, avatar, game_map):
        if self.get_position(avatar.x_position, avatar.y_position, game_map) == "DRAGON":
            game_map[avatar.y_position][avatar.x_position] = "dragon killed"
            print("Message: Dragon killed!")
        else:
            print("Message: There's no any dragons to kill over here.")
    
    def print_messages(self, avatar, game_map):
        if self.get_position(avatar.x_position, avatar.y_position, game_map) == "DRAGON":
            print(f"Alert: You have found a Dragon! Kill him! |{avatar.y_position},{avatar.x_position}|")
        elif self.get_position(avatar.x_position, avatar.y_position, game_map) == "dragon killed":
            print(f"Message: You have killed this Dragon! Well done! |{avatar.y_position},{avatar.x_position}|")
        else:
            print(f"Current Position: You are in {self.get_position(avatar.x_position, avatar.y_position, game_map)} |{avatar.y_position},{avatar.x_position}|")