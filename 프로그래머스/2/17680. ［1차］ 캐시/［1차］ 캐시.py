"""
LRU(Least Recently Used)
    - Hit이면 Cache 맨 앞으로 이동
    - Miss면 Cache 맨 앞에 추가
"""
from collections import deque


def solution(cacheSize, cities):
    cache = deque([], maxlen=cacheSize)
    exec_time = 0
    for city in cities:
        city = city.lower()
        if city in cache:   # hit
            cache.remove(city)
            cache.appendleft(city)
            exec_time += 1
        else:   # miss
            cache.appendleft(city)
            exec_time += 5
            
    return exec_time