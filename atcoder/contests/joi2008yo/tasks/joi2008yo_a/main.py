coins = [500, 100, 50, 10, 5, 1]

price = int(input())
rest_price = 1000 - price

res = 0

for coin in coins:
    while rest_price >= coin:
        rest_price = rest_price - coin
        res = res + 1
print(res)