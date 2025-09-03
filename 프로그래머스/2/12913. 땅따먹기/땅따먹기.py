# 값 누적
def solution(land):
    for row in range(1, len(land)):
        for col in range(4):
            land[row][col] += max([land[row-1][e] for e in range(4) if e != col])
    
    return max(land[-1])