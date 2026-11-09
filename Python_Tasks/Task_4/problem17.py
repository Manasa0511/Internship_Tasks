# Problem 17: Finding the percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input())

student_marks = {}

for i in range(n):
    name, *marks = input().split()
    scores = list(map(float, marks))
    student_marks[name] = scores

query_name = input()

average = sum(student_marks[query_name]) / len(student_marks[query_name])

print("{:.2f}".format(average))
