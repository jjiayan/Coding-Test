import sys
input = sys.stdin.readline

def solve():
    string = input()
    for s in string:
        # 대문자 
        if ord(s) >= 65 and ord(s) <= 90: 
            print(chr((ord(s) + 13) if (ord(s) + 13 <= 90) else 65 + (ord(s) + 13) % 90 - 1), end='') 
        # 소문자
        elif ord(s) >= 97 and ord(s) <= 122:
            print(chr((ord(s) + 13) if (ord(s) + 13 <= 122) else 97 + (ord(s) + 13) % 122 - 1), end='') 
        # 나머지
        else:
            print(s, end='')

if __name__ == "__main__":
    solve()