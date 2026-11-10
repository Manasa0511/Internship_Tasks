# Problem 17: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
a = set(map(int, input().split()))

n = int(input())

result = True

for _ in range(n):
    b = set(map(int, input().split()))

    if not a.issuperset(b) or a == b:
        result = False
        break
      print(result)
