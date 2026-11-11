# Problem 4: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem
def funnyString(s):
    r = s[::-1]

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"

    return "Funny"

t = int(input())

for _ in range(t):
    s = input()
    print(funnyString(s))
