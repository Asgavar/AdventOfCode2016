# --- Day 4: Security Through Obscurity ---
#
# --- Part Two ---
#
# With all the decoy data out of the way, it's time to decrypt this list and get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
#
# What is the sector ID of the room where North Pole objects are stored?


import string

with open("input/D4.txt") as file:
    lines = file.read().split()   # list of lines

alphabet = string.ascii_lowercase   # all leters in the English alphabet


for line in lines:
    checksum_start = line.index("[")
    checksum = line[checksum_start:].replace("[", "").replace("]", "")

    room_name = line[:checksum_start - 3]   # last 3 digits stands for a room number

    room_number = line[checksum_start - 3 : checksum_start]
    room_number = int(room_number)  # must be a number to iterate

    decrypted_line = ""

    for char in room_name:
        if char == "-":
            char = " "
            decrypted_line += char
        else:
            char_position = alphabet.index(char)
            for i in range(room_number):
                char_position += 1
                if char_position == len(alphabet):  # if exceeds by 1
                    char_position = 0

            decrypted_line += alphabet[char_position]   # letter after rotation

    decrypted_line += " " + str(room_number)

    print(decrypted_line)
