def is_valid(text):
    p = {']': '[', '}': '{', ')': '('}
    stack = []
    for t in text:
        if t in p.values():
            stack.append(t)
        else:
            if stack and stack[-1] == p[t]:
                stack.pop()
            else:
                return False
    
    return False if stack else True

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        text = (s * 2)[i:i + len(s)]
        if is_valid(text):
            answer += 1
    
    return answer