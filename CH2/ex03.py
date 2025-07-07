def RANGE(*args):
    if len(args) == 1:
        start, end, step = 0, float(args[0]), 1
    elif len(args) == 2:
        start, end, step = float(args[0]), float(args[1]), 1
    elif len(args) == 3:
        start, end, step = float(args[0]), float(args[1]), float(args[2])
    else:
        return []
    
    if step == 0:
        return []

    result = []
    i = start
    if step > 0:
        while i < end:
            result.append(round(float(i), 3))
            i += step
    else:
        while i > end:
            result.append(round(float(i), 3))
            i += step
    return tuple(result)

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))