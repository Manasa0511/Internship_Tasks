# Problem 11 : Two Strings
# HackerRank Link: https://www.hackerrank.com/challenges/two-strings/problem
def twoStrings(s1, s2):
    if set(s1).intersection(set(s2)):
        return "YES"
    return "NO"

p = int(input())

for _ in range(p):
    s1 = input().strip()
    s2 = input().strip()

    print(twoStrings(s1, s2))
