# https://atcoder.jp/contests/arc017/tasks/arc017_1
# A - 素数、コンテスト、素数

N = int(input())

prime = []
is_prime = []

for i in range(N + 1):
    is_prime.append(True)

is_prime[0] = False
is_prime[1] = False

for i in range(2, N + 1):
    if is_prime[i]:
        prime.append(i)

        j = 2 * i
        while j <= N:
            is_prime[j] = False
            j = j + i

if is_prime[N]:
    print("YES")
else:
    print("NO")

