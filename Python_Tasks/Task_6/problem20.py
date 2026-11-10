# Problem 20: Validating phone numbers
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
n = int(input())

for _ in range(n):
    phone = input()

    if len(phone) == 10 and phone[0] in "789" and phone.isdigit():
        print("YES")
    else:
        print("NO")
