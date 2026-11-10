# Problem 3: Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]
    s = input()
    i, c = input().split()
    result = mutate_string(s, int(i), c)
    print(result)
if __name__ == '__main__':
