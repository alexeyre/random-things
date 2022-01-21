coins = [200, 100, 50, 20, 10, 5, 2, 1]

amount = 47

coins_chosen = []

while amount != 0:
    x = next(filter(lambda x: x <= amount, coins))
    coins_chosen.append(x)
    amount -= x

print(coins_chosen)
print(sum(coins_chosen))
