# --- Day 2: Bathroom Security ---
#
# --- Part Two ---
#
# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:
#
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
#
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:
#
#     You start at "5" and don't move at all (up and left are both edges), ending at 5.
#     Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
#     Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
#     Finally, after five more moves, you end at 3.
#
# So, given the actual keypad layout, the code would be 5DB3.
#
# Using the same instructions in your puzzle input, what is the correct bathroom code?



with open("input/D2.txt") as file:
    instructions = file.read().split()

keypad = [  # a list of lists, each list is a row
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "]
]

pressing = [2, 0]   # row and column of the current button, starting with 5


def up():
    global pressing
    row = pressing[0]
    column = pressing[1]
    row_over = keypad[pressing[0] - 1] if row != 0 else keypad[row]   # not the top
    if not row == 0 and row_over[column] != " ":
        pressing[0] -= 1

def down():
    global pressing
    row = pressing[0]
    column = pressing[1]
    row_under = keypad[pressing[0] + 1] if row != len(keypad) - 1 else keypad[row]   # not the bottom
    if not row == len(keypad) - 1 and row_under[column] != " ":
        pressing[0] += 1

def left():
    global pressing
    row = pressing[0]
    column = pressing[1]
    previous_char_in_row = keypad[row][pressing[1] - 1] if column != 0 else " "   # not the first
    if not previous_char_in_row == " ":
        pressing[1] -= 1

def right():
    global pressing
    row = pressing[0]
    column = pressing[1]
    next_char_in_row = keypad[row][pressing[1] + 1] if column != len(keypad[row]) - 1 else " "   # not the last
    if not next_char_in_row == " ":
        pressing[1] += 1


movements = {
    "U": up,
    "D": down,
    "L": left,
    "R": right
}


code = ""

for line in instructions:
    for character in line:
        movements[character]()  # call a function to move the finger

    row = pressing[0]
    column = pressing[1]

    print(pressing)
    button = keypad[row][column]
    code += str(button)

print("Code to the bathroom is: " + code)
