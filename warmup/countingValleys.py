
def counting_valleys(n, s):
    level = 0
    viz = [0]
    valleys = 0

    for i in range(n):
        if s[i] == 'D':
            level -= 1
            viz.append(level)
        elif s[i] == 'U':
            level += 1
            viz.append(level)

    for j in range(n):
        if (viz[j] < 0) and (viz[j+1] == 0):
            valleys += 1
    return valleys


counting_valleys(8, 'UDDDUDUU')