# --- Day 3: Squares With Three Sides ---
#
# --- Part Two ---
#
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
#
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?



def triangle_or_not(sides):
    longest_side = max(sides[0], sides[1], sides[2])
    sides.remove(longest_side)   # leave the other two
    return True if longest_side < sum(sides) else False


with open("D3.txt") as file:
    lines = file.read().split("\n")   # with spaces at the beginning of each line

sides_as_strings = [line.split() for line in lines][:len(lines)-1]   # because the last line is  empty
sides_as_ints = [[int(side) for side in line] for line in sides_as_strings]

first_column = [sides[0] for sides in sides_as_ints]
second_column = [sides[1] for sides in sides_as_ints]
third_column = [sides[2] for sides in sides_as_ints]


side_sets = []
for i in range(0, len(first_column) - 1, 3):   # all three colums has the same length
    first_new_set = first_column[i:i+3]
    second_new_set = second_column[i:i+3]
    third_new_set = third_column[i:i+3]

    side_sets.append(first_new_set)
    side_sets.append(second_new_set)
    side_sets.append(third_new_set)

triangles = filter(triangle_or_not, side_sets)
count = len(list(triangles))

print("This time, " + str(count) + " of them are triangles.")
