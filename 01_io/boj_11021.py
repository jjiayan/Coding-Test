import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for i in range(1, t+1):
        a, b = list(map(int, input().split()))
        print(f"Case #{i}: {a+b}")
        
if __name__ == "__main__":
    solve()