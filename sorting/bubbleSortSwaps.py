a = [4,2,3,1]

num_swaps = 0
length_arr = len(a)

for j in range(length_arr):
    for i in range(length_arr - 1):
        if a[i] > a[i + 1]:
            num_swaps += 1
            print("Array: {}".format(a))
            print("Swapping {} and {}. Num swaps: {}".format(a[i], a[i + 1], num_swaps))
            a[i], a[i + 1] = a[i + 1], a[i]

print(a)
print("Array is sorted in {} swaps.".format(num_swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[length_arr - 1]))
