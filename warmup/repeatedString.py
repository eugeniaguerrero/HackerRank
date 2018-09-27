def repeated_string(s, n):
    string = [s] * n
    flat_list = [item for sublist in string for item in sublist]
    counter = 0

    for i in range(n):
        if flat_list[i] == 'a':
            print("Found a letter 'a' at pos {}".format(i))
            counter += 1
    print(counter)
    return counter


repeated_string('aba', 10)

