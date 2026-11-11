# Problem 15: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem
from collections import Counter

s = input().strip()

freq = Counter(s)

odd_count = 0

for count in freq.values():
    if count % 2 != 0:
        odd_count += 1

if odd_count <= 1:
    print("YES")
else:
    print("NO")
