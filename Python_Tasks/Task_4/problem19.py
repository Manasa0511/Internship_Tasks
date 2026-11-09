# Problem 19: collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

X = int(input())
shoes = Counter(map(int, input().split()))

N = int(input())
total = 0

for i in range(N):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        total += price
        shoes[size] -= 1

print(total)
