def solution(people, limit):
    left, right = 0, len(people) - 1
    people.sort(reverse=True)
    
    # 몸무게가 가장 큰 사람부터 뽑고 가능한 작은 사람 데려가기
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1
        
        left += 1
    
    return left