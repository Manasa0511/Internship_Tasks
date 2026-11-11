# Problem 10: CamelCase
# HackerRank Link: https://www.hackerrank.com/challenges/camelcase/problem
s = input().strip()

count = 1

for char in s:
    if char.isupper():
        count += 1

print(count)
