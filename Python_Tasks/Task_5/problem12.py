# Problem 12: Capitalize!
# HackerRank Link: https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))
    s = input()
    print(solve(s))

if __name__ == '__main__':
