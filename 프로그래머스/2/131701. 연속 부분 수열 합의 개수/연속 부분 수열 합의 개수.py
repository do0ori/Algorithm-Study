def solution(elements):
    answer = set()
    
    for window_size in range(1, len(elements) + 1):
        for pivot in range(len(elements)):
            end = pivot + window_size
            if end > len(elements):
                group = elements[pivot:] + elements[:end % len(elements)]
            else:
                group = elements[pivot:end]
            answer.add(sum(group))
    
    return len(answer)
