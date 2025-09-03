from collections import deque

def solution(x, y, n):
    visited = set([y])
    queue = deque([(y, 0)])
    while queue:
        num, step = queue.popleft()
        if num == x: return step
        
        if num - n >= x and (num - n) not in visited:
            queue.append((num - n, step + 1))
            visited.add(num - n)
        if num % 2 == 0 and num / 2 >= x and (num / 2) not in visited:
            queue.append((num / 2, step + 1))
            visited.add(num / 2)
        if num % 3 == 0 and num / 3 >= x and (num / 3) not in visited:
            queue.append((num / 3, step + 1))
            visited.add(num / 3)
    
    return -1