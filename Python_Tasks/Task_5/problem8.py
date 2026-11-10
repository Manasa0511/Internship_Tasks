# Problem 8: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem
n = int(input())
countries = set()

for i in range(n):
    countries.add(input())

print(len(countries))
