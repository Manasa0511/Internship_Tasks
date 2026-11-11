# Problem 13: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
from collections import Counter

s = input().strip()

freq = Counter(s)
values = list(freq.values())

counts = Counter(values)

if len(counts) == 1:
    print("YES")

elif len(counts) == 2:
    (f1, c1), (f2, c2) = counts.items()

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        print("YES")
    elif abs(f1 - f2) == 1 and (c1 == 1 or c2 == 1):
        print("YES")
    else:
        print("NO")

else:
    print("NO")
