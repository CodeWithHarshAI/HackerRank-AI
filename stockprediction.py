#!/usr/bin/env python3
import math

def compute_slope(y):
    x = [1, 2, 3, 4, 5]
    n = 5

    x_mean = sum(x) / n
    y_mean = sum(y) / n

    num = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    den = sum((x[i] - x_mean) ** 2 for i in range(n))

    return num / den if den != 0 else 0


def printTransactions(m, k, d, names, owned, prices):
    slope_list = []

    for i in range(k):
        slope = compute_slope(prices[i])
        slope_list.append(slope)

    sorted_indices = sorted(range(k), key=lambda i: slope_list[i])

    amount_remaining = m
    trans = {}

    # BUY (positive trend)
    for idx in reversed(sorted_indices):
        if slope_list[idx] > 0 and amount_remaining >= prices[idx][-1]:
            price = prices[idx][-1]
            num_stock = int(amount_remaining // price)

            if num_stock > 0:
                amount_remaining -= price * num_stock
                trans[names[idx]] = f"{names[idx]} BUY {num_stock}"

    # SELL (negative trend)
    for idx in sorted_indices:
        if slope_list[idx] < 0 and owned[idx] > 0:
            trans[names[idx]] = f"{names[idx]} SELL {owned[idx]}"

    print(len(trans))
    for key in trans:
        print(trans[key])


if __name__ == '__main__':
    m, k, d = input().split()
    m = float(m)
    k = int(k)
    d = int(d)

    names = []
    owned = []
    prices = []

    for _ in range(k):
        temp = input().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(x) for x in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)
