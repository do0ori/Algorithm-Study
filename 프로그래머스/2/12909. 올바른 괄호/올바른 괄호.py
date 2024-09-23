def solution(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:   # c == ')'
            if stack:
                stack.pop()
            else:
                return False
    
    return True if not stack else False