import sys
input = sys.stdin.readline

def solve():
    string = input().rstrip()
    arr = []
    
    for i in range(len(string)):
        arr.append(string[i:])
    
    print(*(sorted(arr)), sep='\n')
    

if __name__ == "__main__":
    solve()