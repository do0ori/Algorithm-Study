# 겹치는 곳에 카메라 설치
def solution(routes):
    routes.sort()
    cam = routes[0] # 카메라를 범위로 할당
    answer = 1
    for route in routes:
        if route[0] <= cam[1]:    # 겹치는 범위 구하기
            cam[0] = max(cam[0], route[0])
            cam[1] = min(cam[1], route[1])
        else:   # 새로운 카메라 범위 추가
            cam = route
            answer += 1
    
    return answer