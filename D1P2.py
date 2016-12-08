# --- Day 1: No Time for a Taxicab ---
#
# --- Part Two ---
#
# Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?


with open("input/D1.txt") as file:
    instructions = file.read().replace(",", "").split()

facing = 0   # north
location = [0, 0]
visited = list()   # contains already visited locations
found = False

def north(howfar):
    global location
    location[1] += howfar   # y

def east(howfar):
    global location
    location[0] += howfar   # x

def south(howfar):
    global location
    location[1] -= howfar # y

def west(howfar):
    global location
    location[0] -= howfar   # x


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

    for i in range(0, howfar):  # go block by block
        directions[facing](1)  # call a function to go

        if location in visited:   # if already visited
            first_twice = list(location)
            found = True
            break

        visited.append(list(location))   # appends a copy of the list, not the list itself as a reference

    if found:
        break

x = first_twice[0]
y = first_twice[1]

distance = abs(x) + abs(y)

print("First location visited twice is: x = " + str(x) + " y = " + str(y))
print("Which is " + str(distance) + " blocks away")
