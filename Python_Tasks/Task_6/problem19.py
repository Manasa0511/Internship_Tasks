# Problem 19: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter

s = input()

count = Counter(s)

result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

for char, frequency in result[:3]:
    print(char, frequency)

