# 정수론 & 수학 기초 (Python 코테 기준)

## 1. 에라토스테네스의 체 (Sieve of Eratosthenes)

### 1.1 왜 필요한가?
특정 범위 내의 **모든 소수(Prime Number)**를 찾아야 할 때 가장 효율적인 알고리즘이다. 단순히 하나씩 소수인지 판별하는 방식($O(N\sqrt{N})$)보다 훨씬 빠르며, 대량의 소수 판별이 필요한 문제에서 TLE를 방지하는 핵심 도구다.

---

### 1.2 핵심 원리
1. 2부터 $N$까지의 모든 수를 소수 후보로 둔다.
2. 아직 지워지지 않은 수 중 가장 작은 수 $P$를 찾는다 (이는 소수다).
3. $P$를 제외한 $P$의 배수들을 모두 지운다.
4. $P$를 $N$의 제곱근까지만 반복하며 배수를 지우면, 남은 수들이 모두 소수가 된다.



---

### 1.3 Python 구현 (최적화)
```python
def get_primes(n):
    # 0부터 n까지의 소수 여부를 저장하는 리스트 (True로 초기화)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님
    
    # n의 제곱근까지만 확인하면 됨
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i가 소수라면, i의 배수들을 False로 처리
            # i*i 이전의 배수들은 이미 이전 소수들에 의해 처리됨
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return [i for i, prime in enumerate(is_prime) if prime]
```

---

## 2. 유클리드 호제법 (Euclidean Algorithm)

### 2.1 왜 필요한가?
두 수의 **최대공약수(GCD)**를 구할 때 사용한다. 소인수분해를 이용하는 방식보다 훨씬 빠르며, 두 수가 아무리 커도 $O(\log N)$의 시간 복잡도로 정답을 찾아낸다.

---

### 2.2 핵심 원리
두 수 $a, b$ ($a > b$)에 대하여, $a$를 $b$로 나눈 나머지를 $r$이라고 하면:
**$GCD(a, b) = GCD(b, r)$** 이 성립한다. 이 과정을 나머지가 0이 될 때까지 반복하며, 그때의 나누는 수가 최대공약수다.



[Image of Euclidean algorithm flowchart]


---

### 2.3 Python 구현

#### 2.3.1 반복문 방식 (추천)
```python
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
```

#### 2.3.2 내장 함수 사용 (가장 빠름)
```python
import math
# Python 3.5 이상 지원, 3.9부터는 여러 인자 지원
result = math.gcd(1071, 462) 
```

### 2.4 최소공배수 (LCM)
최대공약수를 활용해 다음 공식으로 구한다.
$$LCM(a, b) = \frac{a \times b}{GCD(a, b)}$$

```python
def lcm(a, b):
    # (a * b) // gcd(a, b) 로 계산
    import math
    return (a * b) // math.gcd(a, b)
```

---

## 3. 진법 변환 (Base Conversion)

### 3.1 10진수 → n진수 (직접 구현)
10진수 값을 n으로 더 이상 나눌 수 없을 때까지 나누며 나머지를 기록하고, 이를 역순으로 읽는다.

```python
def decimal_to_n(num, base):
    if num == 0: return '0'
    
    digits = "0123456789ABCDEF"
    result = ""
    
    while num > 0:
        num, mod = divmod(num, base)
        result += digits[mod]
        
    return result[::-1] # 뒤집어서 반환
```

---

### 3.2 n진수 → 10진수 (내장 함수)
Python의 `int()` 함수는 두 번째 인자로 진법을 받아 정수로 변환해준다.

```python
# int(문자열, 진법)
print(int('1011', 2))   # 11
print(int('212', 3))    # 23
print(int('FF', 16))    # 255
```

---

### 3.3 내장 진법 변환 함수 (2, 8, 16진수)
결과물에 `0b`, `0o`, `0x` 같은 접두어가 붙는다는 점에 유의한다.

```python
bin(42) # '0b101010' (2진수)
oct(42) # '0o52'     (8진수)
hex(42) # '0x2a'     (16진수)

# 접두어를 제거하고 숫자만 필요한 경우 슬라이싱 사용
bin(42)[2:] # '101010'
```

---

## 4. 핵심 알고리즘 요약표

| 알고리즘 | 목적 | 시간 복잡도 | 주요 특징 |
| :--- | :--- | :--- | :--- |
| **에라토스테네스의 체** | 범위 내 모든 소수 구하기 | $O(N \log \log N)$ | 메모리를 사용하여 속도를 확보함 |
| **유클리드 호제법** | 최대공약수(GCD) 추출 | $O(\log N)$ | `math.gcd` 활용 권장 |
| **진법 변환** | 숫자의 표기법 변경 | $O(\log_{base} N)$ | `int(s, n)`과 `divmod` 활용 |

---

## 💡 코테 꿀팁
* **소수 판별:** 한두 개의 숫자만 판별할 때는 에라토스테네스의 체보다 **제곱근까지만 나누어 보는 방식**($O(\sqrt{N})$)이 훨씬 효율적
* **복잡도 인지:** 유클리드 호제법은 숫자가 $10^{18}$ 정도로 커도 순식간에 계산되므로 안심하고 사용
* **진법 문제:** 3진법이나 5진법 등 비주류 진법 문제는 `divmod`를 활용한 직접 구현이 가장 빠르고 정확

