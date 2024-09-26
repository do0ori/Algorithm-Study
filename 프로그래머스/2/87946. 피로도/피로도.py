from itertools import permutations

def solution(k, dungeons):
    dungeon_orders = list(permutations(dungeons))
    
    max_count = 0
    for dungeons in dungeon_orders:
        count = 0
        fatigue = k
        for dungeon in dungeons:
            if fatigue < dungeon[0]:
                break
            else:
                fatigue -= dungeon[1]
                count += 1
                
        max_count = max(count, max_count)
        
        if max_count == len(dungeons):
            break
    
    return max_count