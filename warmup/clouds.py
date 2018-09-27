def jumping_on_clouds(c):
    counter = 0

    print(c)

    i = 0
    while i < (len(c) - 1):
        if (i + 2 < len(c)) and c[i + 2] != 1:
            counter += 1
            print("Jumping to current pos {} + 2 steps".format(i))
            i += 2
        elif (i + 1 < len(c)) and c[i + 1] != 1:
            counter += 1
            print("Jumping to current pos {} + 1 step".format(i))
            i += 1
        else:
            print("All done")
            break

    print(counter)
    return counter


jumping_on_clouds([0, 1, 0, 1, 0, 1, 0])

