class item:
    def __init__(self, name, type, damage, defense, fun):
        self.name = name
        self.type = type
        self.damage = damage
        self.defense = defense
        self.fun = fun

items = []
craftables = []

combinations = [["fire", "water", "mercury"], ["fire", "earth", "sulfur"], ["water", "earth", "salt"]]

pen = item("pen", "weapon", 1, 0, 0)
thing = item("thing", "weapon", 0, 0, 0)

items.append(pen)
items.append(thing)

# Add more items manually
sword = item("sword", "weapon", 7, 0, 1)
items.append(sword)

gun = item("gun", "weapon", 9, 0, 2)
items.append(gun)

shield = item("shield", "armor", 0, 6, 1)
items.append(shield)

apple = item("apple", "food", 0, 0, 3)
items.append(apple)

book = item("book", "misc", 0, 0, 4)
items.append(book)

lamp = item("lamp", "misc", 0, 0, 2)
items.append(lamp)

knife = item("knife", "weapon", 5, 0, 0)
items.append(knife)

hat = item("hat", "armor", 0, 3, 1)
items.append(hat)

shirt = item("shirt", "armor", 0, 4, 1)
items.append(shirt)

shoes = item("shoes", "armor", 0, 2, 1)
items.append(shoes)

gloves = item("gloves", "armor", 0, 1, 1)
items.append(gloves)

socks = item("socks", "armor", 0, 1, 0)
items.append(socks)

belt = item("belt", "armor", 0, 2, 0)
items.append(belt)

pants = item("pants", "armor", 0, 3, 0)
items.append(pants)

tshirt = item("tshirt", "armor", 0, 2, 0)
items.append(tshirt)

dress = item("dress", "armor", 0, 1, 1)
items.append(dress)

phone = item("phone", "misc", 0, 0, 5)
items.append(phone)

cup = item("cup", "misc", 0, 0, 1)
items.append(cup)

pen_holder = item("pen_holder", "misc", 0, 0, 1)
items.append(pen_holder)

watch = item("watch", "misc", 0, 0, 2)
items.append(watch)

wallet = item("wallet", "misc", 0, 0, 3)
items.append(wallet)

glasses = item("glasses", "misc", 0, 0, 2)
items.append(glasses)

headphones = item("headphones", "misc", 0, 0, 3)
items.append(headphones)

guitar = item("guitar", "weapon", 6, 0, 3)
items.append(guitar)

keyboard = item("keyboard", "weapon", 8, 0, 4)
items.append(keyboard)

microphone = item("microphone", "weapon", 7, 0, 4)
items.append(microphone)

bottle = item("bottle", "misc", 0, 0, 1)
items.append(bottle)

candle = item("candle", "misc", 0, 0, 1)
items.append(candle)

plate = item("plate", "misc", 0, 0, 1)
items.append(plate)

fork = item("fork", "misc", 0, 0, 1)
items.append(fork)

spoon = item("spoon", "misc", 0, 0, 1)
items.append(spoon)

knife = item("knife", "misc", 0, 0, 1)
items.append(knife)

bowl = item("bowl", "misc", 0, 0, 1)
items.append(bowl)

teapot = item("teapot", "misc", 0, 0, 1)
items.append(teapot)

paintbrush = item("paintbrush", "misc", 0, 0, 2)
items.append(paintbrush)

easel = item("easel", "misc", 0, 0, 3)
items.append(easel)

canvas = item("canvas", "misc", 0, 0, 2)
items.append(canvas)

laptop = item("laptop", "misc", 0, 0, 4)
items.append(laptop)

headset = item("headset", "misc", 0, 0, 4)
items.append(headset)

monitor = item("monitor", "misc", 0, 0, 3)
items.append(monitor)

keyboard = item("keyboard", "misc", 0, 0, 2)
items.append(keyboard)

mouse = item("mouse", "misc", 0, 0, 1)
items.append(mouse)

printer = item("printer", "misc", 0, 0, 2)
items.append(printer)

paper = item("paper", "misc", 0, 0, 1)
items.append(paper)

scissors = item("scissors", "misc", 0, 0, 1)
items.append(scissors)

chair = item("chair", "misc", 0, 0, 1)
items.append(chair)

table = item("table", "misc", 0, 0, 1)
items.append(table)

couch = item("couch", "misc", 0, 0, 1)
items.append(couch)

lamp = item("lamp", "misc", 0, 0, 1)
items.append(lamp)

rug = item("rug", "misc", 0, 0, 1)
items.append(rug)

vase = item("vase", "misc", 0, 0, 1)
items.append(vase)

plant = item("plant", "misc", 0, 0, 1)
items.append(plant)

painting = item("painting", "misc", 0, 0, 2)
items.append(painting)

statue = item("statue", "misc", 0, 0, 2)
items.append(statue)

clock = item("clock", "misc", 0, 0, 2)
items.append(clock)

mirror = item("mirror", "misc", 0, 0, 1)
items.append(mirror)

candlestick = item("candlestick", "misc", 0, 0, 1)
items.append(candlestick)

flowerpot = item("flowerpot", "misc", 0, 0, 1)
items.append(flowerpot)

photo_frame = item("photo_frame", "misc", 0, 0, 1)
items.append(photo_frame)

mirror = item("air", "misc", 0, 0, 1)
items.append(mirror)

candlestick = item("fire", "misc", 0, 0, 1)
items.append(candlestick)

flowerpot = item("water", "misc", 0, 0, 1)
items.append(flowerpot)

photo_frame = item("earth", "misc", 0, 0, 1)
items.append(photo_frame)

photo_frame = item("ether", "misc", 0, 0, 1)
craftables.append(photo_frame)

flowerpot = item("salt", "misc", 0, 0, 1)
craftables.append(flowerpot)

photo_frame = item("sulfur", "misc", 0, 0, 1)
craftables.append(photo_frame)

photo_frame = item("mercury", "misc", 0, 0, 1)
craftables.append(photo_frame)