# --- Day 6: Signals and Noise ---
#
# --- Part Two ---
#
# Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.
#
# In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.
#
# In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.
#
# Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?


with open("input/D6.txt") as file:
    lines = file.read().split()


password = str()

for i in range(len(lines[0])):  # iterate through columns, since all lines has the same length
    column_letters = str()
    for line in lines:
        column_letters += line[i]

    occurences = {c: column_letters.count(c) for c in column_letters}
    occurences = list(occurences.items())
    occurences = sorted(occurences, key = lambda x: x[1])   # all that had to be modified xD

    password += occurences[0][0]


print("Message sent: " + password)
