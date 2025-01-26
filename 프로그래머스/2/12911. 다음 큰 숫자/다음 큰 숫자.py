def solution(n):
    count1 = bin(n).count('1')
    for i in range(n + 1, 2 * n + 1):
        if bin(i).count('1') == count1:
            return i