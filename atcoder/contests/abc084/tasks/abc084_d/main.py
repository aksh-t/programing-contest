# D - 2017-like Number
# https://atcoder.jp/contests/abc084/tasks/abc084_d

prime = []
is_prime = []
is_prime.append(False)
is_prime.append(False)

def sieve(r):
    for i in range(2, r + 1):
        is_prime.append(True)

    for i in range(2, r + 1):
        if is_prime[i]:
            prime.append(i)

            j = 2 * i
            while j <= r:
                is_prime[j] = False
                j = j + i

def main():
    Q = int(input())
    querys = []
    max_r = 0
    for i in range(Q):
        l, r = map(int, input().split())
        querys.append((l, r))
        if max_r < r:
            max_r = r

    sieve(max_r)

    for l, r in querys:
        like_numbers = [n for n in prime if n % 2 == 1 and l <= n <= r and is_prime[(n + 1) // 2]]
        print(len(like_numbers))
    
main()