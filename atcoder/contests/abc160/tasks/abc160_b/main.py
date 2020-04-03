# B - Golden Coins
# https://atcoder.jp/contests/abc160/tasks/abc160_b

X = int(input())

count_500, X = divmod(X, 500)
count_5 = X // 5

print(count_500 * 1000 + count_5 * 5)
