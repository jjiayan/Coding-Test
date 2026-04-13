import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.arr = []
    
    def push(self, value):
        self.arr.append(value)
    
    def pop(self):
        if self.size() != 0: return self.arr.pop()
        return -1
    
    def size(self):
        return len(self.arr)
    
    def empty(self):
        if self.size() == 0: return 1
        return 0
    
    def top(self):
        if self.size() != 0: return self.arr[-1]
        return -1 

def solve():
    stack = Stack()
    
    n = int(input())
    for _ in range(n):
        x = input().rstrip()
        if x == 'top': print(stack.top())
        elif x == 'empty': print(stack.empty())
        elif x == 'size': print(stack.size())
        elif x == 'pop': print(stack.pop())
        else: 
            _, v = x.split()
            stack.push(v)
        

if __name__ == "__main__":
    solve()