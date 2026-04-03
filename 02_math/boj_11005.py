import sys
input = sys.stdin.readline

def solve():
    n, b = map(int, input().split())
    result = ''
    # 10진법
    if b == 10:
        print(n)
        return
    else:
        while n >= b:
            n, m = divmod(n, b) # 몫, 나머지
            result += chr(m+55) if m >= 10 else str(m)
    result += chr(n+55) if n >= 10 else str(n)
    print(*result[::-1], sep='')

if __name__ == "__main__":
    solve()