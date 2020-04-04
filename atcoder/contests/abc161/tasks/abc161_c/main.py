N, K = map(int, input().split())

min_num = N % K if N % K < abs(N % K - K) else abs(N % K - K)

print(str(min_num))