import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for i in range(1, 2 * n):
        if i <= n:
            print(' ' * (n - i) + '*' * i)
        else:
            i -= n
            print(' ' * i + '*' * (n - i))

if __name__ == "__main__":
    solve()