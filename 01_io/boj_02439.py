import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * i)

if __name__ == "__main__":
    solve()