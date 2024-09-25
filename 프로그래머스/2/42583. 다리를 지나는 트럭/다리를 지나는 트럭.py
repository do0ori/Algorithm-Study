from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge_stack = deque([0] * bridge_length)
    wait_stack = deque(truck_weights)
    passed = []
    count = 0
    
    while wait_stack:
        bridge_stack.popleft()
        
        if sum(bridge_stack) + wait_stack[0] <= weight:
            bridge_stack.append(wait_stack.popleft())
        else:
            bridge_stack.append(0)
            while bridge_stack[0] == 0:
                bridge_stack.popleft()
                bridge_stack.append(0)
                count += 1
        count += 1
    
    return count + bridge_length
