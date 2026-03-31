# 입출력 최적화 & 문자열 처리 (Python 코테 기준)

## 1. 왜 입출력 최적화가 필요한가?

Python의 기본 `input()`은 내부적으로 `sys.stdin.readline()`을 래핑하지만, 매번 flush를 수행하고 프롬프트 처리 등 부가 비용이 있다. 입력이 수만~수십만 줄인 문제에서는 이 차이가 TLE(Time Limit Exceeded)로 이어진다.

---

## 2. sys.stdin 기본 사용법

### 2.1 모듈 임포트

```python
import sys
input = sys.stdin.readline
```

이 한 줄로 이후 코드에서 `input()`을 그대로 쓰면서 빠른 I/O를 쓸 수 있다.

> **주의**: `sys.stdin.readline()`은 줄 끝에 `\n`을 포함한다. `int(input())`은 괜찮지만, 문자열로 받을 때는 `.strip()`이 필요하다.

### 2.2 정수 한 줄 입력

```python
n = int(input())
```

### 2.3 공백으로 구분된 정수 여러 개

```python
a, b = map(int, input().split())
```

### 2.4 정수 리스트

```python
arr = list(map(int, input().split()))
```

### 2.5 n줄 입력 → 리스트

```python
n = int(input())
data = [int(input()) for _ in range(n)]
```

---

## 3. EOF(End of File) 처리

입력 줄 수가 주어지지 않고 EOF까지 읽어야 하는 문제.

### 방법 1: try-except

```python
import sys
input = sys.stdin.readline

while True:
    try:
        line = input().strip()
        if not line:
            continue
        # 처리
    except EOFError:
        break
```

### 방법 2: sys.stdin 전체 읽기 (가장 빠름)

```python
import sys

data = sys.stdin.read().split()
idx = 0

# data[idx], data[idx+1] ... 순서대로 파싱
```

`sys.stdin.read()`는 전체 입력을 한 번에 읽어 문자열로 반환한다. `.split()`하면 공백/줄바꿈 모두 구분자로 처리되어 토큰 배열이 된다. 반복 입력이 매우 많을 때 가장 빠른 방법이다.

### 방법 3: sys.stdin 이터레이터

```python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # 처리
```

---

## 4. 출력 최적화

### 4.1 print vs sys.stdout.write

`print()`는 매번 flush하지 않지만, 호출 오버헤드가 있다. 출력이 수만 줄이면 문자열을 한 번에 모아서 출력하는 것이 훨씬 빠르다.

```python
import sys
output = []

for i in range(n):
    output.append(str(result))

print('\n'.join(output))
# 또는
sys.stdout.write('\n'.join(output) + '\n')
```

### 4.2 f-string 포맷 출력

```python
# Case #1: 결과
print(f"Case #{i}: {result}")

# 소수점 고정
print(f"{value:.6f}")
```

---

## 5. 자주 쓰는 입력 패턴 모음

### 5.1 2차원 배열 (격자 입력)

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
```

### 5.2 문자열 격자 (미로 등)

```python
n = int(input())
maze = [input().strip() for _ in range(n)]
# maze[r][c] 로 접근
```

### 5.3 그래프 간선 입력

```python
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
```

---

## 6. 문자열 처리

### 6.1 split / strip

```python
s = "  hello world  "
s.split()        # ['hello', 'world'] — 공백 기준, 빈 문자열 무시
s.strip()        # 'hello world' — 양쪽 공백 제거
s.split(' ')     # ['', '', 'hello', 'world', '', ''] — 정확히 공백 하나 기준
```

> 코테에서는 거의 항상 `split()`(인자 없음)을 쓴다.

### 6.2 join

```python
arr = [1, 2, 3]
' '.join(map(str, arr))   # '1 2 3'
'\n'.join(map(str, arr))  # '1\n2\n3'
```

### 6.3 문자열 → 리스트 / 리스트 → 문자열

```python
s = "abcde"
lst = list(s)          # ['a', 'b', 'c', 'd', 'e']
''.join(lst)           # 'abcde'
```

### 6.4 문자열 뒤집기

```python
s[::-1]
```

### 6.5 문자 카운트

```python
from collections import Counter
cnt = Counter("hello")  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
cnt['l']                # 2
```

### 6.6 ord / chr

```python
ord('a')   # 97
ord('A')   # 65
chr(97)    # 'a'

# 알파벳 인덱스 (0-based)
idx = ord(c) - ord('a')
```

### 6.7 문자열 탐색

```python
s = "hello world"
s.find("world")       # 6 (없으면 -1)
s.index("world")      # 6 (없으면 ValueError)
"world" in s          # True
s.startswith("he")    # True
s.endswith("ld")      # True
s.count("l")          # 3
```

### 6.8 문자열 치환

```python
s.replace("l", "L")        # 'heLLo worLd'
s.replace("l", "L", 1)     # 'heLlo world' — 최대 1번
```

### 6.9 대소문자

```python
s.upper()    # 'HELLO WORLD'
s.lower()    # 'hello world'
s.isalpha()  # True/False — 알파벳만
s.isdigit()  # True/False — 숫자만
s.isalnum()  # True/False — 알파벳 또는 숫자
```

---

## 7. 속도 비교 요약

| 방법 | 속도 | 비고 |
|------|------|------|
| `input()` | 느림 | 기본 함수 |
| `sys.stdin.readline` | 빠름 | 한 줄씩 읽기 |
| `sys.stdin.read()` | 가장 빠름 | 전체 한 번에 읽기 |
| `print()` 여러 번 | 느림 | 반복 출력 |
| `'\n'.join()` + `print` 1번 | 빠름 | 모아서 한 번 출력 |

---

## 8. 보일러플레이트 (코테 시작 템플릿)

```python
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solve():
    n = int(input())
    # ...

solve()
```

입력이 매우 많을 때:

```python
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    for _ in range(m):
        a, b = int(data[idx]), int(data[idx+1])
        idx += 2
        # ...

solve()
```

---

## 9. 자주 하는 실수

| 실수 | 원인 | 해결 |
|------|------|------|
| `\n` 포함된 문자열 | `readline()`은 `\n` 포함 | `.strip()` 또는 `int()` 변환 |
| 빈 줄 무시 안 함 | EOF/빈 줄 처리 누락 | `if not line: continue` |
| 출력 순서 뒤섞임 | `sys.stdout.write` 후 flush 미수행 | 마지막에 `sys.stdout.flush()` 또는 `print` 사용 |
| 문자열을 숫자로 비교 | `split()` 후 타입이 `str` | `map(int, ...)` 적용 |
