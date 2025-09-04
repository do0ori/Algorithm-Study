from collections import defaultdict
from math import ceil

def solution(fees, records):
    cars = defaultdict(list)
    for record in records:
        time, car_num, status = record.split()
        h, m = time.split(':')
        minutes = int(h) * 60 + int(m)
        cars[car_num].append(minutes)
    
    answer = dict()
    base_time, base_fee, unit_time, unit_fee = fees
    for car_num, time_list in cars.items():
        parking_duration = 0
        if len(time_list) % 2 != 0:
            time_list.append(23 * 60 + 59)
        for i in range(0, len(time_list), 2):
            duration = time_list[i + 1] - time_list[i]
            parking_duration += duration
        answer[car_num] = base_fee + (ceil((parking_duration - base_time) / unit_time) * unit_fee if parking_duration > base_time else 0)
    sorted_answer = sorted(answer.items())
    
    return [a[1] for a in sorted_answer]