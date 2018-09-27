from collections import deque


def rot_left(a, d):
    rotations = a[1]
    queue = deque(d)

    while rotations > 0:
        queue.append(queue[0])
        queue.popleft()
        rotations -= 1

    return queue

