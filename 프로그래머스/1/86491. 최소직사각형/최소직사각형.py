def solution(sizes):
    shorter_max = longer_max = 0
    
    for size in sizes:
        if size[0] < size[1]:
            shorter, longer = size
        else:
            longer, shorter = size
        
        shorter_max, longer_max = max(shorter, shorter_max), max(longer, longer_max)
    
    return shorter_max * longer_max