# 내 풀이가 더 빠르다
def solution(n, wires):
    neighbor = dict()
    for tower1, tower2 in wires:
        neighbor[tower1] = [*neighbor.get(tower1, []), tower2]
        neighbor[tower2] = [*neighbor.get(tower2, []), tower1]

    result = n
    for tower1, tower2 in wires:
        visited = [tower2]
        stack = [tower1]
        while stack:    # 모든 연결 찾기
            tower = stack.pop()
            if tower not in visited:
                visited.append(tower)
            neighbors = [n for n in neighbor[tower] if n not in visited]
            stack.extend(neighbors)
            
        result = min(result, abs(n - 2 * (len(visited) - 1)))   # 추가한 tower2는 빼줘야하므로 len(visited) - 1
        if result == 0: break   # 최선의 정답
        
    return result

# 다른 풀이 참고
def other_solution(n, wires):
    result = n
    
    # wire 하나를 제거한 wires list
    rest_wires_list = list(wires[i+1:] + wires[:i] for i in range(len(wires)))
    
    for rest_wires in rest_wires_list:
        wires_set = set(rest_wires[0])
        for _ in rest_wires:    # 모든 연결을 찾기 위해 rest_wires 만큼 반복
            for wire in rest_wires: # wire마다 연결 찾기
                if set(wire) & wires_set:   # 교집합이 존재 = 연결되어 있다
                    wires_set.update(wire)  # 추가
                    
        result = min(result, abs(2 * len(wires_set) - n))
        if result == 0: break   # 최선의 정답
        
    return result