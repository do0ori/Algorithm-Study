def solution(s):
    answer = []
    space_idx = -1
    for i in range(len(s)):
        if s[i] == ' ':
            space_idx = i
            answer.append(s[i])
        else:
            if i - 1 == space_idx:  # 첫 문자
                if s[i] in range(10):   # 숫자면
                    answer.append(s[i])
                else:
                    answer.append(s[i].upper())
            else:
                answer.append(s[i].lower())
    
    return ''.join(answer)