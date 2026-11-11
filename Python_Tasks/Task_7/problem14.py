# Problem 14: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem
from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    first = s[:n // 2]
    second = s[n // 2:]

    count1 = Counter(first)
    count2 = Counter(second)

    changes = 0

    for char in count1:
        if count1[char] > count2[char]:
            changes += count1[char] - count2[char]

    return changes

q = int(input())

for _ in range(q):
    s = input().strip()
    print(anagram(s))
