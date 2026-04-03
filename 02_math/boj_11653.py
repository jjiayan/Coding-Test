import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    if n == 1: return
    i = 2
    
    while n > 1:
        if n % i == 0:
            print(i)
            n //= i
        else:
            i += 1

if __name__ == "__main__":
    solve()