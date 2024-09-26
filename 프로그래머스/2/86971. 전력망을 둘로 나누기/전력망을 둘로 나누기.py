def solution(n, wires):
    neighbor = dict()
    for tower1, tower2 in wires:
        neighbor[tower1] = [*neighbor.get(tower1, []), tower2]
        neighbor[tower2] = [*neighbor.get(tower2, []), tower1]

    result = n
    for tower1, tower2 in wires:
        visited = [tower2]
        stack = [tower1]
        while stack:
            tower = stack.pop()
            if tower not in visited:
                visited.append(tower)
            neighbors = [n for n in neighbor[tower] if n not in visited]
            stack.extend(neighbors)
            
        result = min(result, abs(n - 2 * (len(visited) - 1)))
        
        if result == 0:
            break
        
    return result