def solution(arr):
    arr.sort(reverse=True)
    num = 1
    while True:
        multiple = arr[0] * num
        cnt = 0
        for a in arr:
            if multiple % a == 0:
                cnt += 1
        
        if cnt == len(arr):
            return multiple
    
        num += 1