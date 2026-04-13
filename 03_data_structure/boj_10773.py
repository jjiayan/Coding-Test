import sys
input = sys.stdin.readline

def solve():
    arr = []
    k = int(input())
    for _ in range(k):
        n = int(input())
        if n != 0: arr.append(n)
        else: arr.pop()
    print(sum(arr))
            
if __name__ == "__main__":
    solve()