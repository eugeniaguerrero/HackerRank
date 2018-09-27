prices = [1, 2, 3, 4]
k = 7

total_sum = 0
toys = []
for elem in sorted(prices):
    if k < total_sum:
        total_sum += elem
        toys.append(elem)
    else:
        print(toys)

