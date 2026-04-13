import sys
input = sys.stdin.readline

def solve():
    arr = [1]
    cal = ['+']
    n = int(input())
    cur = 1
    for _ in range(n):
        x = int(input())
        
        # cur < x
        if cur < x:
            for i in range(cur+1, x+1):
                arr.append(i)
                cal.append('+')
            cur = x
                
        # arr 마지막 값과 같을 때
        if x == arr[-1]:
            arr.pop()
            cal.append('-')
            
    if not arr: print(*cal, sep='\n')
    else: print('NO')

if __name__ == "__main__":
    solve()