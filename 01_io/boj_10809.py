import sys
input = sys.stdin.readline

def solve():
    word = input().rstrip()
    arr = [-1 for _ in range(26)]
    
    for i, s in enumerate(word):
        if arr[ord(s) - 97] == -1:
            arr[ord(s) - 97] = i
    
    print(*arr)

if __name__ == "__main__":
    solve()