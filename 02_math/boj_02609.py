import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    gcd, lcm = 1, min(a, b)
    # 최대 공약수 gcd 
    for i in range(lcm, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    # 최소 공배수 lcm
    for j in range(max(a, b), a * b + 1):
        if j % a == 0 and j % b == 0:
            lcm = j
            break
        
    print(gcd, lcm, sep='\n')
            

if __name__ == "__main__":
    solve()