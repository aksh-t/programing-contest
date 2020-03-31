# D - 2017-like Number
# https://atcoder.jp/contests/abc084/tasks/abc084_d

prime = []
is_prime = []
is_prime.append(False)
is_prime.append(False)

def sieve(r):
    start = len(is_prime)
    if start >= r:
        return 

    for i in range(start, r + 1):
        is_prime.append(True)

    for i in prime:
        j = 2 * i
        while j <= r:
            if j < start:
                j = j + i
                continue

            is_prime[j] = False
            j = j + i

    for i in range(start, r + 1):
        if is_prime[i]:
            prime.append(i)

            j = 2 * i
            while j <= r:
                is_prime[j] = False
                j = j + i

def main():
    answers = []
    Q = int(input())
    for i in range(Q):
        l, r = map(int, input().split())
        sieve(r)
        like_numbers = [n for n in prime if n % 2 == 1 and l <= n <= r and is_prime[(n + 1) // 2]]
        answers.append(len(like_numbers))
    
    for answer in answers:
        print(answer)

main()