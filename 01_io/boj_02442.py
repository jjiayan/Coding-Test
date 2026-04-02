import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for i in range(1, n):
        b = n - i
        m = 2 * i - 1
        print(' ' * b + '*' * m + ' ')
    print('*' * (2 * n - 1))

if __name__ == "__main__":
    solve()