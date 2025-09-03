# native solution => time out
"""
def get_bigger_num(n, num_list):
    while num_list:
        back = num_list.pop()
        if n < back:
            return back
    return -1

def solution(numbers):
    return [get_bigger_num(n, numbers[i+1:][::-1]) for i, n in enumerate(numbers)]
"""
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 아직 뒷 큰수를 찾지 못한 index
    for i, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            answer[stack.pop()] = n
        stack.append(i)
    
    return answer