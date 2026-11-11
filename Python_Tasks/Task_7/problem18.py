# Problem 18: String Construction
# HackerRank Link: https://www.hackerrank.com/challenges/string-construction/problem
n = int(input())

for _ in range(n):
    s = input().strip()

    print(len(set(s)))
