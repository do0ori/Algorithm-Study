def solution(msg):
    dictionary = {w: i + 1 for i, w in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    answer = []
    i = 0
    while i < len(msg):
        w = msg[i]
        while i + 1 < len(msg) and (w + msg[i + 1]) in dictionary:
            i += 1
            w += msg[i]
        
        answer.append(dictionary[w])
        if i + 1 < len(msg):
            c = msg[i + 1]
            dictionary[w + c] = len(dictionary) + 1
        
        i += 1
    
    return answer