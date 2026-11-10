# Problem 14: Finding the percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *marks = input().split()
        student_marks[name] = list(map(float, marks))

    query_name = input()

    average = sum(student_marks[query_name]) / 3

    print(f"{average:.2f}")
