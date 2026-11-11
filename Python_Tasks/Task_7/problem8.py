# Problem 8: Gemstones
# HackerRank Link: https://www.hackerrank.com/challenges/gem-stones/problem
n = int(input())

gemstones = set(input().strip())

for _ in range(n - 1):
    rock = set(input().strip())
    gemstones = gemstones.intersection(rock)

print(len(gemstones))
