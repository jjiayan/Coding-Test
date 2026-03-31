import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    nums = input().strip()
    result = 0
    for i in nums:
        result += int(i)
    print(result)
    

if __name__ == "__main__":
    solve()