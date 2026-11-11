# Problem 6: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem
s = input().lower()

if set("abcdefghijklmnopqrstuvwxyz").issubset(set(s)):
    print("pangram")
else:
    print("not pangram")
