# Problem 18: The Minion Game
# HackerRank Link: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(s):
    kevin = 0
    stuart = 0

    n = len(s)

    for i in range(n):
        if s[i] in "AEIOU":
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
