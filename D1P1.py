with open("D1.txt") as file:
    instructions = file.read().replace(",", "").split()

facing = 0   # north
x = 0   # coordinates
y = 0   #


def north(howfar):
    global y
    y += howfar

def east(howfar):
    global x
    x += howfar

def south(howfar):
    global y
    y -= howfar

def west(howfar):
    global x
    x -= howfar


directions = {0: north,  # maps functions to ints
              1: east,
              2: south,
              3: west
              }


for instruction in instructions:
    turn = instruction[0]
    howfar = int(instruction[1:])

    facing += 1 if turn == "R" else -1
    if facing == 4:   # "loops" directions
        facing = 0
    if facing == -1:
        facing = 3

    directions[facing](howfar)  # call a function to go

print ("x = " + str(x))
print ("y = " + str(y))

distance = x + y
print ("distance = " + str(distance))
