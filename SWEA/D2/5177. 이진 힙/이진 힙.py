# heapq.heapify로 검증 가능
def heapify(arr):
    heap = []

    for a in arr:
        heap.append(a)
        current = len(heap) - 1  # 추가한 원소의 index

        while current > 0:  # Root 노드 도달 시 종료
            parent = (current - 1) // 2
            if heap[parent] > heap[current]:
                heap[parent], heap[current] = heap[current], heap[parent]
                current = parent
            else:
                break

    return heap


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = heapify(map(int, input().split()))

    answer = 0
    node = len(numbers) - 1
    while node > 0:
        node = (node - 1) // 2  # 조상
        answer += numbers[node]

    print(f"#{test_case} {answer}")
