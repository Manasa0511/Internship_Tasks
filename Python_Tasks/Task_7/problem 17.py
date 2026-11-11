# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem
def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]
        num = int(first)

        current = first

        while len(current) < len(s):
            num += 1
            current += str(num)

        if current == s:
            print("YES", first)
            return

    print("NO")

q = int(input())

for _ in range(q):
    s = input().strip()
    separateNumbers(s)
