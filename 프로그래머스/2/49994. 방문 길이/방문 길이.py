def solution(dirs):
    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    x = y = 0
    paths = set()
    for d in dirs:
        dx, dy = directions[d]
        if -5 <= x + dx <= 5 and -5 <= y + dy <= 5:
            p1 = (x, y)
            x = x + dx
            y = y + dy
            p2 = (x, y)
            print(p1, p2)
            paths.add((p1, p2))
            paths.add((p2, p1))
        else:
            continue
    return len(paths) // 2