array_1 = [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]


def get_sum(items):
    sum_of_items = 0
    for elem in items:
        sum_of_items += elem
    return sum_of_items


def hourglass_sum(arr):
    arr = array_1
    hourglass_sums = [0] * 16
    counter = 0

    for col in range(4):
        for row in range(4):
            print("This is index [{}][{}], counting hourglass {}".format(row, col, counter))
            print("[{}][{}] = {}, [{}][{}] = {}, [{}][{}] = {}".format(row, col, arr[row][col],
                                                                       row, (col + 1), arr[row][col + 1],
                                                                       row, (col + 2), arr[row][col + 2]))

            print("            [{}][{}] = {}               ".format((row + 1), (col + 1), (arr[row + 1][col + 1])))

            print("[{}][{}] = {}, [{}][{}] = {}, [{}][{}] = {}".format((row + 2), col, arr[row + 2][col],
                                                                       (row + 2), (col + 1), arr[row + 2][col + 1],
                                                                       (row + 2), (col + 2), arr[row + 2][col + 2]))
            hourglass_sums[counter] = get_sum(items=[arr[row][col],
                                                     arr[row][col + 1],
                                                     arr[row][col + 2],
                                                     arr[row + 1][col + 1],
                                                     arr[row + 2][col],
                                                     arr[row + 2][col + 1],
                                                     arr[row + 2][col + 2]])
            counter += 1

    biggest_elem = 0
    for elem in hourglass_sums:
        if elem > biggest_elem:
            biggest_elem = elem

    return biggest_elem



