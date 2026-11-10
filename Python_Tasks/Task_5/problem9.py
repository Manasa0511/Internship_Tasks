# Problem 9: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem
n = int(input())

words = {}
order = []

for i in range(n):
    word = input()

    if word not in words:
        words[word] = 0
        order.append(word)

    words[word] += 1

print(len(words))
print(*[words[word] for word in order])
