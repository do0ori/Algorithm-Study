def solution(number, k):
    stack = []
    
    # 현재 수보다 앞에 있는 작은 수 모두 제거
    for n in number:
        while stack and stack[-1] < n and k != 0:
            stack.pop()
            k -= 1

        stack.append(n)
    
    # k개 만큼 제거되지 않은 경우 뒤에서 제거
    return ''.join(stack if not k else stack[:-k])
    
    