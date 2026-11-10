# Problem 1: Find the Runner-Up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
arr = list(map(int, input().split()))

unique_scores = sorted(set(arr))

print(unique_scores[-2])
