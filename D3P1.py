# --- Day 3: Squares With Three Sides ---
#
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?


def triangle_or_not(sides):
    longest_side = max(sides[0], sides[1], sides[2])
    sides.remove(longest_side)   # leave the other two
    return True if longest_side < sum(sides) else False


with open("D3.txt") as file:
    lines = file.read().split("\n")   # with spaces at the beginning of each line

sides_as_strings = [line.split() for line in lines][:len(lines)-1]   # because the last line is  empty
sides_as_ints = [[int(side) for side in line] for line in sides_as_strings]

triangles = filter(triangle_or_not, sides_as_ints)
count = len(list(triangles))

print(str(count) + " of them are triangles.")
