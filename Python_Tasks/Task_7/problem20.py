# Problem 20: Super Reduced String
# HackerRank Link: https://www.hackerrank.com/challenges/reduced-string/problem
def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = "".join(stack)

    if result == "":
        return "Empty String"

    return result

s = input().strip()

print(superReducedString(s))
