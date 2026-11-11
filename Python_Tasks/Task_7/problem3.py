# Problem 3: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem
s = input()

count = 0

for i in range(len(s)):
    if s[i] != "SOS"[i % 3]:
        count += 1

print(count)
