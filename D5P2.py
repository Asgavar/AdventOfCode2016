# --- Day 5: How About a Nice Game of Chess? ---
#
# --- Part Two ---
#
# As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution.
#
# Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position.
#
# A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.
#
# For example, if the Door ID is abc:
#
#     The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
#     In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
#     The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
#
# You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.
#
# Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation.


import hashlib

door_id = b"ugkcyxxp"   # no input file here
password = ["-"] * 8   # 8 digits
password_found = False
i = 0   # integer that will be increasing

while not password_found:
    h = hashlib.md5(door_id + str(i).encode())
    h = h.hexdigest()

    first_five = h[:5]

    if first_five == "00000":
        position = h[5]
        if not position in "01234567":
            i += 1  # otherwise would freeze here
            continue

        if password[int(position)] == "-":   # only if this position is empty
            print("New letter found: " + h[6] + " on position " + position)
            password[int(position)] = h[6]   # 7th char is the value

    already_found = [c for c in password if c != "-"]
    if len(already_found) == 8:
        password_found = True

    i += 1


password = "".join(password)
print("And the password is: " + password)
