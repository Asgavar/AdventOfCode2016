# --- Day 1: No Time for a Taxicab ---
#
#
# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
#
# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
#
# For example:
#
#     Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
#     R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
#     R5, L5, R5, R3 leaves you 12 blocks away.
#
# How many blocks away is Easter Bunny HQ?


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
