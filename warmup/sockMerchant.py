import math
import os
import random
import re
import sys
import array


def is_unseen(n, ar):
    for i in range(len(ar)):
        if n == ar[i]:
            return False
    return True


# Complete the sockMerchant function below.
def sock_merchant(n, ar):
    counter = [0] * 100

    for sock_type in ar:
        counter[sock_type] += 1

    num_pairs = 0

    for count in counter:
        num_pairs += int(count/2)

    return num_pairs


sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])

