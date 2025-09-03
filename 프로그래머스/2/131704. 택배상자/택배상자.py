def solution(order):
    boxes = list(range(len(order), 0, -1))
    belt = []
    i = 0
    while i < len(order):
        if belt and order[i] == belt[-1]:
            belt.pop()
            i += 1
        elif boxes:
            box = boxes.pop()
            if order[i] != box:
                belt.append(box)
            else:
                i += 1
        else:
            break

    return i