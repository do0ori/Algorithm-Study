alphabet = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 12,
    'P': 11,
    'Q': 10,
    'R': 9,
    'S': 8,
    'T': 7,
    'U': 6,
    'V': 5,
    'W': 4,
    'X': 3,
    'Y': 2,
    'Z': 1,
}

def solution(name):    
    change_cnt = 0
    for n in name:
        change_cnt += alphabet[n]
    
    # 한 번 방문
    r_last_not_A_idx = 0
    for i in range(len(name) - 1, -1, -1):
        if name[i] != 'A':
            r_last_not_A_idx = i
            break
    case_r = r_last_not_A_idx   # 오른쪽 이동
    
    l_last_not_A_idx = 0
    for i in range(1, len(name)):
        if name[i] != 'A':
            l_last_not_A_idx = i
            break
    case_l = len(name) - l_last_not_A_idx   # 왼쪽 이동
    
    move = min(case_r, case_l)
    
    # 두 번 방문
    l_not_A_idx = 0
    min_move = move
    for i, n in enumerate(name):
        if n != 'A':
            l_not_A_idx = i
        
        r_not_A_idx = l_not_A_idx + 1
        while r_not_A_idx < len(name) and name[r_not_A_idx] == 'A':
            r_not_A_idx += 1
        
        case_rl = l_not_A_idx * 2 + len(name) - r_not_A_idx     # 오른쪽 이동 후 돌아와서 왼쪽 이동
        case_lr = (len(name) - r_not_A_idx) * 2 + l_not_A_idx   # 왼쪽 이동 후 돌아와서 오른쪽 이동
        min_move = min(min_move, case_rl, case_lr)
    
    return change_cnt + min_move
        
        
    
    