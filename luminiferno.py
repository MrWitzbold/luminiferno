import lumilib
import random
import pickle
import types

# next: add alchemy elements, make a synthesize function and make the player able to make new items

def save():
    state = {'globals': {}, 'locals': {}}
    for var_name, var_value in globals().items():
        if not isinstance(var_value, types.ModuleType):
            state['globals'][var_name] = var_value
    for var_name, var_value in locals().items():
        if not isinstance(var_value, types.ModuleType):
            state['locals'][var_name] = var_value
    with open("save.pk1", 'wb') as file:
        pickle.dump(state, file)

def load():
    with open("save.pk1", 'rb') as file:
        state = pickle.load(file)
    globals().update(state['globals'])
    locals().update(state['locals'])

player = 0

directions = ["North", "South", "East", "West", "Nyxis", "Vexel", "Elda", "Stela", "Crypt", "Ethos"]

zone_items_took = []

class player_instance:
    def __init__(self, name, health, weapon, item, armor, inventory, coordinate):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.item = item
        self.armor = armor
        self.inventory = inventory
        self.coordinate = coordinate

def get_items(zone_coordinate):
    seed_str = "1"
    for i in range(0, len(zone_coordinate)):
        seed_str += str(zone_coordinate[i])
        seed_str += "1"
    seed = int(seed_str)
    random.seed(seed)
    items_available = []
    item_chances = random.randint(0, 20)
    for i in range(0, item_chances):
        if random.randint(0, 10) % 2 == 0:
            items_available.append(lumilib.items[random.randint(0, len(lumilib.items)-1)])
    return items_available

def zone(coordinate):
    print("\n===============================================================")
    print("You are in the " + str(player.coordinate) + " zone")
    items_available = get_items(player.coordinate)
    items_str = ""
    items_took = []
    for zone in zone_items_took:
        if zone[0] == coordinate:
            items_took.append(zone[1])
    for i in range(len(items_available)-1):
        item = items_available[i]
        if item.name not in items_took:
            if i != len(items_available)-1:
                items_str += item.name + ", "
            else:
                items_str += item.name
    print("Items in zone: " + items_str)
    print("\n\n===============================================================")

def execute_command(command):
    if command == "help":
        print("\n\nAvailable commmands:\n")
        print("create_character (for first time playing)")
        print("save")
        print("load")
        print("walk {direction 1 to 10} {amount of steps}")
        print("(backwards) walkb {direction 1 to 10} {amount of steps}")
        print("take {Item name}")
        print("inv - displays inventory")
        print("throw {item name} - throws away every item with that name")
        print("conjunction {item name} {item name}")
        print("distill {item name}")

    if command == "create_character":
        print("\n\nYou are creating your character")
        print("\nWhat will you be called? ")
        name = input("")
        print("\nOkay, " + name + ", welcome to luminiferno")
        global player
        player = player_instance(name, 100, "", "", [], [], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    if (command.startswith("walk") or command.startswith("walkb")) and player != 0:
        direction = command.split(" ")[1]
        amount = command.split(" ")[2]
        if command.split(" ")[0] != "walkb":
            player.coordinate[int(direction)-1] += int(amount)
            print("You walked " + amount + " steps into " + directions[int(direction)-1])
        else:
            player.coordinate[int(direction)-1] -= int(amount)
            print("You walked " + amount + " steps away from " + directions[int(direction)-1])

    if command.startswith("check") and player != 0:
        print("\nYou have " + str(player.health) + " health")
        print("You have the {" + str(player.weapon) + "} weapon equippted.")
        print("You have the {" + str(player.item) + "} item equippted.")
        print("You have the {" + str(player.armor) + "} armor equippted.")
        print("You have the following items: " + str((player.inventory)))

    if command.startswith("take") and player != 0:
        items_available = get_items(player.coordinate)
        took = False
        for item in items_available:
            if item.name == command.split(" ")[1]:
                player.inventory.append(item)
                print("You took " + item.name)
                took = True
                zone_items_took.append([player.coordinate, item.name])
                break
        if took == False:
            print("This isn't an item in this zone.")

    if command.startswith("inv") and player != 0:
        items_str = ""
        for i in range(0, len(player.inventory)):
            item = player.inventory[i]
            if i!= len(player.inventory)-1:
                items_str += item.name + ", "
            else:
                items_str += item.name
        print("Your inventory: " + items_str)

    if command.startswith("save") and player!= 0:
        save()

    if command.startswith("load"):
        load()

    if command.startswith("throw") and player!= 0:
        for item in player.inventory:
            if item.name == command.split(" ")[1]:
                player.inventory.remove(item)
                print("You threw away " + item.name)
                break

    if command.startswith("conjunction") and player!= 0:
        item1_name = command.split(" ")[1]
        item2_name = command.split(" ")[2]
        combined = ""
        for combination in lumilib.combinations:
            if (combination[0] == item1_name and combination[1] == item2_name) or (combination[0] == item2_name and combination[1] == item1_name):
                combined = combination[2]

        if combined != "":
            for item in player.inventory:
                if item.name == command.split(" ")[1]:
                    for item2 in player.inventory:
                        if item2.name == command.split(" ")[2]:
                            player.inventory.remove(item)
                            player.inventory.remove(item2)
                            print("You conjured " + combined)
                            for item in lumilib.craftables:
                                if item.name == combined:
                                    player.inventory.append(item)
                            break
        else:
            print("You can't make anything from those.")

    if command.startswith("distill") and player!= 0:
        for combination in lumilib.combinations:
            if combination[2] == command.split(" ")[1]:
                for item in player.inventory:
                    if item.name == command.split(" ")[1]:
                        player.inventory.remove(item)
                        print("You distilled " + combination[2])
                        for item in lumilib.items:
                            if item.name == combination[0]:
                                player.inventory.append(item)
                            if item.name == combination[1]:
                                player.inventory.append(item)
                        for item in lumilib.craftables:
                            if item.name == combination[0]:
                                player.inventory.append(item)
                            if item.name == combination[1]:
                                player.inventory.append(item)


while True:
    if(player == 0):
        print("\n\nWelcome to luminiferno. Say help for the commands\n")
    else:
        zone(player.coordinate)
    print("\n\n$: ")
    command = input("")
    execute_command(command)