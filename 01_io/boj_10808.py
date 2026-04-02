import sys
input = sys.stdin.readline

def solve():
    word = input().strip()
    arr = [0 for _ in range(26)]
    
    for s in word:
        arr[ord(s) - 97] += 1
    
    print(*arr)
    
if __name__ == "__main__":
    solve()