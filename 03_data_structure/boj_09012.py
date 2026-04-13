import sys
input = sys.stdin.readline

def vps(x):
    arr = []
    for i in x:
        if i == '(': 
            arr.append(i)
        elif i == ')' and arr:
            arr.pop()
        else:
            return False
    if arr: return False
    return True
            
def solve():
    t = int(input())
    for _ in range(t):
        ps = input().rstrip()
        if vps(ps): print("YES")
        else: print("NO")

if __name__ == "__main__":
    solve()