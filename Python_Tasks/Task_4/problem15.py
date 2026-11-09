# Problem 15: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem
n = int(input())

words = {}

for i in range(n):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values())
