import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    expression = input().strip()
    nums = {chr(i+65): int(input()) for i in range(n)}
    stack = []
    
    for i in expression:
        if i == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(a + b)
        elif i == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif i == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:
            stack.append(nums[i])
    print('%.2f'%stack[-1])

    

if __name__ == "__main__":
    solve()