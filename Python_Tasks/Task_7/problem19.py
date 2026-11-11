# Problem 19: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
s = input().strip()

n = int(input())

weights = set()

count = 0
previous = ""

for char in s:
    if char == previous:
        count += 1
    else:
        count = 1

    weight = (ord(char) - ord('a') + 1) * count
    weights.add(weight)

    previous = char

for _ in range(n):
    x = int(input())

    if x in weights:
        print("Yes")
    else:
        print("No")
