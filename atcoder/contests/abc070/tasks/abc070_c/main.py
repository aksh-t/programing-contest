N = int(input())
Ts = list(set([int(input()) for _ in range(N)]))

def get_divider(n):
    divider = set()
    for i in range(1, n):
        if i * i > n:
            break

        if n % i == 0:
            divider.add(i)
            if i != int(n / i):
                divider.add(int(n / i))
    return divider


divider_set = set()
for T in Ts:
    divider_set = divider_set.union(get_divider(T))
divider_set.discard(1)
print(str(min(divider_set)))

