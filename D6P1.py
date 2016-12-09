# --- Day 6: Signals and Noise ---
#
# Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.
#
# In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.
#
# All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:
#
# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
#
# The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.
#
# Given the recording in your puzzle input, what is the error-corrected version of the message being sent?


with open("input/D6.txt") as file:
    lines = file.read().split()


password = str()

for i in range(len(lines[0])):  # iterate through columns, since all lines has the same length
    column_letters = str()
    for line in lines:
        column_letters += line[i]

    occurences = {c: column_letters.count(c) for c in column_letters}
    occurences = list(occurences.items())
    occurences = sorted(occurences, key = lambda x: x[1], reverse = True)

    password += occurences[0][0]


print("Message sent: " + password)
