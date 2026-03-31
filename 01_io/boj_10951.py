import sys

def solve():
    for line in sys.stdin:
        a, b = list(map(int, line.split()))
        print(a + b)

if __name__ == "__main__":
    solve()