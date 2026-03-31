import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        a, b = list(map(int, input().split()))
        print(a + b)

if __name__ == "__main__":
    solve()