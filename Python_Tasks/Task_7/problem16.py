# Problem 16: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem
n = int(input())
s = input().strip()
k = int(input())

k = k % 26

result = ""

for char in s:
    if 'a' <= char <= 'z':
        result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))

    elif 'A' <= char <= 'Z':
        result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))

    else:
        result += char

print(result)
