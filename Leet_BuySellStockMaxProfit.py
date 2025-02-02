prices = [7,1,5,3,6,4]
minPrice = prices[0]
profit = 0

for p in prices[1:]:
    if p > minPrice:
        profit = max(profit, p - minPrice)
    minPrice = min(minPrice, p)

print(profit)