from collections import deque


def is_convertable(s1, s2):
    diff_cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_cnt += 1
    
    return True if diff_cnt == 1 else False

def bfs(begin, target, words):
    visit = set([begin])
    queue = deque([begin])
    cnt = 0
    
    while queue:
        for _ in range(len(queue)):
            q = queue.popleft()
            print(q)
            
            if q == target:
                return cnt  # 변환 완료 & 횟수 반환
            
            for word in words:
                if is_convertable(q, word): # 변환 가능한 단어
                    if word not in visit:
                        visit.add(word)
                        queue.append(word)
        
        cnt += 1
        print(cnt)
    
    return 0    # 변환 불가능
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)