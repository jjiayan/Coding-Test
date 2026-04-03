import sys
input = sys.stdin.readline

def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False 
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime
    # return [i for i, prime in enumerate(is_prime) if prime]

def solve():
    cnt = [0] * (123456 * 2 + 1)
    for i, p in enumerate(get_primes(123456 * 2)[1:]):
        if p:
            cnt[i+1] = cnt[i] + 1
        else:
            cnt[i+1] = cnt[i]

    while True:
        n = int(input())
        if n == 0:
            return
        
        print(cnt[2*n] - cnt[n])

if __name__ == "__main__":
    solve()