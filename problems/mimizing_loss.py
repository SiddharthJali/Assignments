price = [20, 15, 7, 2, 13]

min_loss = 99999
buy, sell = 0, 0

for i in range(len(price)):
    for j in range((i+1), len(price)):
        if price[i] > price[j]:
            loss = price[i] - price[j]
            if loss < min_loss:
                min_loss = loss
                buy = i+1
                sell = j+1

print(f"Buy at year {buy} and Sell at year {sell}, Minimum Loss will be: {min_loss}")
