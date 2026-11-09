# Problem 9: Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    return "".join(a)
if __name__ == '__main__':
