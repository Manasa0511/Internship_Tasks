# Problem 6: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    return sum(set(array)) / len(set(array))

    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

if __name__ == '__main__':
