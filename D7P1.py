# --- Day 7: Internet Protocol Version 7 ---
#
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
#
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.
#
# For example:
#
#     abba[mnop]qrst supports TLS (abba outside square brackets).
#     abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
#     aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
#     ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
#
# How many IPs in your puzzle input support TLS?

import re

with open("input/D7.txt") as file:
    lines = file.read().split()


abba_pattern = r"(\w)(\w)\2\1"
hypernet_pattern = r"\[.*?\]"   # "[", then something, then "]"
four_same_pattern = r"(.)(\1){3,}"

supporting_tls = 0

for line in lines:

    if re.search(four_same_pattern, line):
        line = re.sub(four_same_pattern, "", line)   # cut them from the line

    hypernets = re.findall(hypernet_pattern, line)
    rest = re.sub(str(hypernets), "", line)   # not sure why it didn't work for the hypernet_pattern, but well, it works now

    is_hypernet_abba = re.search(abba_pattern, str(hypernets))
    if is_hypernet_abba:
        continue

    else:
        is_rest_abba = re.search(abba_pattern, rest)
        if is_rest_abba:
            supporting_tls += 1


print(str(supporting_tls) + " of them support TLS")
