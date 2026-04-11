def solution(balance: str) -> str:
    restored = []
    digit_sum = 0

    for ch in balance:
        if ch.isdigit():
            restored.append(ch)
            digit_sum += int(ch)
        elif ch == "A":
            add = str(digit_sum)
            restored.append(add)
            digit_sum += sum(int(c) for c in add)
        else:  # ch == 'B'
            last = int(restored[-1][-1])
            prev = int(restored[-1][-2]) if len(restored[-1]) >= 2 else int(restored[-2][-1])
            add = str(abs(prev - last))
            restored.append(add)
            digit_sum += sum(int(c) for c in add)

    return "".join(restored)
