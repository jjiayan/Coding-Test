# 자료구조 기초: 스택 (Python 코테 기준)

## 1. 스택 (Stack) — LIFO 구조

### 1.1 왜 필요한가?

스택은 **나중에 넣은 것이 먼저 나오는(LIFO: Last In, First Out)** 자료구조다. 재귀적으로 처리해야 하는 문제, 되돌아가야 하는 문제, 현재 상태를 저장하고 복원해야 하는 문제에서 핵심 도구로 사용된다.

---

### 1.2 핵심 원리

| 연산 | 설명 | Python | 시간 복잡도 |
| :--- | :--- | :--- | :--- |
| `push` | 스택 최상단에 원소 추가 | `stack.append(x)` | $O(1)$ |
| `pop` | 스택 최상단 원소 제거 & 반환 | `stack.pop()` | $O(1)$ |
| `peek` | 최상단 원소 확인 (제거 X) | `stack[-1]` | $O(1)$ |
| `is_empty` | 스택이 비어있는지 확인 | `not stack` | $O(1)$ |

---

### 1.3 Python 구현

Python의 `list`는 스택으로 사용하기에 최적이다. `append()`와 `pop()`이 모두 $O(1)$이므로 별도의 클래스 없이 바로 사용한다.

```python
stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
# stack = [1, 2, 3]

# peek (최상단 확인)
top = stack[-1]   # 3 (제거 X)

# pop
val = stack.pop() # 3 반환, stack = [1, 2]

# 비었는지 확인
if not stack:
    print("스택이 비었습니다")
```

> **주의**: `stack.pop(0)`은 $O(N)$이므로 큐(Queue) 동작이 필요하다면 `collections.deque`를 사용한다.

---

## 2. 괄호 검증 (Bracket Validation)

### 2.1 왜 필요한가?

여는 괄호와 닫는 괄호가 올바르게 쌍을 이루는지 검사하는 문제다. "가장 최근에 열린 괄호"와 현재 닫는 괄호가 짝이 맞아야 한다는 조건이 LIFO 구조와 정확히 일치하므로 스택이 최적의 해법이다.

---

### 2.2 핵심 원리

1. 여는 괄호 `(`, `[`, `{`를 만나면 스택에 `push`한다.
2. 닫는 괄호 `)`, `]`, `}`를 만나면 스택 최상단을 꺼내 짝이 맞는지 확인한다.
3. 짝이 맞지 않거나, 스택이 비어있는데 닫는 괄호가 등장하면 **유효하지 않음**.
4. 모든 문자를 처리한 후 스택이 **비어있어야** 유효함.

---

### 2.3 Python 구현

#### 단일 괄호 검증 (백준 9012)

```python
import sys
input = sys.stdin.readline

def is_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:  # c == ')'
            if not stack:
                return False
            stack.pop()
    return not stack  # 스택이 비어야 유효

t = int(input())
for _ in range(t):
    s = input().strip()
    print("YES" if is_valid(s) else "NO")
```

#### 복합 괄호 검증 `()`, `[]`, `{}`

```python
def is_valid(s):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != pair[c]:
                return False
            stack.pop()

    return not stack
```

---

### 2.4 자주 나오는 변형

| 문제 유형 | 접근법 |
| :--- | :--- |
| 괄호 문자열이 올바른지 판별 | 위 기본 구현 |
| 올바른 괄호 문자열을 만들기 위한 최소 수정 횟수 | 스택에 남은 개수로 계산 (`len(stack)`) |
| 짝이 안 맞는 괄호의 위치 반환 | 스택에 인덱스 저장 |

```python
# 짝이 맞지 않는 인덱스 찾기
def find_invalid(s):
    stack = []  # (문자, 인덱스) 저장
    invalid = set()

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                invalid.add(i)  # 짝 없는 닫는 괄호

    invalid.update(stack)  # 짝 없는 여는 괄호
    return sorted(invalid)
```

---

## 3. 후위 표기식 (Postfix Notation)

### 3.1 표기법 종류

| 표기법 | 예시 | 특징 |
| :--- | :--- | :--- |
| 중위 표기식 (Infix) | `3 + 4 * 2` | 사람이 쓰는 방식, 연산자 우선순위 필요 |
| 전위 표기식 (Prefix) | `+ 3 * 4 2` | 연산자가 앞 |
| 후위 표기식 (Postfix) | `3 4 2 * +` | 연산자가 뒤, 괄호 불필요, 컴퓨터 계산에 최적 |

---

### 3.2 중위 → 후위 변환 (Shunting-yard 알고리즘)

**핵심 원칙**
1. **피연산자(숫자)**: 즉시 출력(결과에 추가)한다.
2. **연산자**: 스택에 push하되, 스택 최상단에 **우선순위가 같거나 높은** 연산자가 있으면 먼저 pop하여 출력한 후 push한다.
3. **`(`**: 무조건 스택에 push한다.
4. **`)`**: `(`가 나올 때까지 스택을 pop하여 출력한다. `(`는 버린다.
5. 입력이 끝나면 스택에 남은 연산자를 모두 pop하여 출력한다.

```python
def infix_to_postfix(expression):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    result = []

    for token in expression:
        if token.isdigit() or token.isalpha():
            # 피연산자: 바로 출력
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            # '('가 나올 때까지 pop
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # '(' 제거
        else:
            # 연산자: 우선순위 비교 후 push
            while (stack and stack[-1] != '(' and
                   stack[-1] in priority and
                   priority[stack[-1]] >= priority[token]):
                result.append(stack.pop())
            stack.append(token)

    # 남은 연산자 모두 출력
    while stack:
        result.append(stack.pop())

    return ' '.join(result)

# 예시: "3 + 4 * 2" → "3 4 2 * +"
tokens = "3 + 4 * 2".split()
print(infix_to_postfix(tokens))  # 3 4 2 * +
```

> **`^` (거듭제곱)** 은 오른쪽 결합이므로 `>=` 대신 `>`로 조건을 바꿔야 한다.

---

### 3.3 후위 표기식 계산

후위 표기식은 **스택 하나만으로** 왼쪽부터 순서대로 처리할 수 있다.

1. 피연산자를 만나면 스택에 push한다.
2. 연산자를 만나면 스택에서 두 개를 pop하여 계산하고, 결과를 다시 push한다.
3. 모든 처리가 끝나면 스택에 최종 결과 하나만 남는다.

```python
def evaluate_postfix(tokens):
    stack = []

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()  # 나중에 꺼낸 것이 오른쪽 피연산자
            a = stack.pop()  # 먼저 꺼낸 것이 왼쪽 피연산자
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b))  # 정수 나눗셈

    return stack[0]

# 예시: "3 4 2 * +" → 11
tokens = "3 4 2 * +".split()
print(evaluate_postfix(tokens))  # 11
```

---

## 4. 핵심 알고리즘 요약표

| 알고리즘 | 목적 | 시간 복잡도 | 공간 복잡도 |
| :--- | :--- | :--- | :--- |
| **괄호 검증** | 괄호 쌍의 유효성 확인 | $O(N)$ | $O(N)$ |
| **중위 → 후위 변환** | Shunting-yard | $O(N)$ | $O(N)$ |
| **후위 표기식 계산** | 스택 기반 계산 | $O(N)$ | $O(N)$ |

---

## 💡 코테 꿀팁

* **스택이 빈 상태에서 pop을 시도하면 IndexError**: 항상 `if stack:` 또는 `if not stack: return False`로 방어한다.
* **pop 순서 주의**: `a op b`를 계산할 때 `b = stack.pop()`, `a = stack.pop()` 순서가 맞아야 한다. 나눗셈, 뺄셈은 순서에 민감하다.
* **단조 스택(Monotone Stack)**: "현재 원소보다 크거나 작은 다음 원소 찾기" 류의 문제에 자주 쓰인다. 스택에 인덱스를 저장하고, 조건을 만족하면 pop하며 답을 기록하는 패턴을 익혀두자.
* **괄호 개수만 세는 최적화**: 단일 종류 괄호(`()`)만 검증할 때는 스택 대신 카운터 변수 하나로 해결 가능하다 (`cnt`가 음수가 되면 즉시 False).

```python
# 단일 괄호 카운터 최적화
def is_valid_fast(s):
    cnt = 0
    for c in s:
        if c == '(': cnt += 1
        else:
            cnt -= 1
            if cnt < 0: return False
    return cnt == 0
```
