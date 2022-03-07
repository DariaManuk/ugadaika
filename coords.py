def coords(x, y):
    c = 0
    d = 0
    x = float(x)
    y = float(y)
    for i in range(17, -1, -1):
        if x < 180 / 2 ** i:
            d = i + 1
            break
    for j in range(17, -1, -1):
        if y < 360 / 2 ** j:
            c = j + 1
            break
    return (c + d) // 2
