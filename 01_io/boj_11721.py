import sys
input = sys.stdin.readline

def solve():
    string = input()
    l = len(string) // 10 if len(string) % 10 == 0 else len(string) // 10 + 1
    for i in range(l-1):
        print(string[i * 10: i * 10 + 10])
    print(string[(l-1) * 10:])

if __name__ == "__main__":
    solve()