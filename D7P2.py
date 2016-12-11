# --- Day 7: Internet Protocol Version 7 ---
#
# --- Part Two ---
#
# You would also like to know which IPs support SSL (super-secret listening).
#
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.
#
# For example:
#
#     aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
#     xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
#     aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
#     zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
#
# How many IPs in your puzzle input support SSL?


import regex

with open("input/D7.txt") as file:
    lines = file.read().split()


aba_pattern = r"(\w)(\w)(\1)"
hypernet_pattern = r"\[.*?\]"   # "[", then something, then "]"
three_same_pattern = r"(.)(\1)(\1)"

supporting_ssl = 0

for line in lines:

    three_same = regex.findall(three_same_pattern, line)
    for th in three_same:
        line = line.replace("".join(th), "")

    hypernets = regex.findall(hypernet_pattern, line)

    supernet = line
    for h in hypernets:
        supernet = supernet.replace(h, "")

    aba_occurences = regex.findall(aba_pattern, supernet, overlapped=True)

    hypernets_text = "".join(hypernets)

    for a in aba_occurences:
        aba = "".join(a)
        bab = aba[1] + aba[0] + aba[1]

        if bab in hypernets_text:
            supporting_ssl += 1
            continue


print(str(supporting_ssl) + " of them support SSL.")   # the correct answer was higher by one in fact
