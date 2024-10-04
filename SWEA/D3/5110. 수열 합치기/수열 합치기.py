# 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력해야 하므로 단순 linked list가 아닌 doubly linked list 사용
class Node:
    def __init__(self, value=None, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, data=[]) -> None:
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

        self.fill_initial_value(data)

    def fill_initial_value(self, data) -> None:
        if type(data) != list:
            data = [data]

        last_node = self.head
        for d in data:
            new_node = Node(d, last_node)
            last_node.next = new_node
            last_node = new_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def insert_with_rule(self, arr) -> None:
        curr_node = self.head.next
        while curr_node.value and curr_node.value <= arr[0]:
            curr_node = curr_node.next

        prev_node = curr_node.prev
        for a in arr:
            new_node = Node(a, prev_node)
            prev_node.next = new_node
            prev_node = new_node
        new_node.next = curr_node
        curr_node.prev = new_node

    def get_10_reverse(self) -> str:
        result = []
        curr_node = self.tail
        for _ in range(10):
            result.append(str(curr_node.prev.value))
            curr_node = curr_node.prev
        return " ".join(result)

    def print_all(self) -> None:
        curr_node = self.head
        while curr_node.next != self.tail:
            curr_node = curr_node.next
            print(curr_node.value, end=" ")
        print()


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    base_arr = DoublyLinkedList(list(map(int, input().split())))
    arrs = [list(map(int, input().split())) for _ in range(M - 1)]

    for arr in arrs:
        base_arr.insert_with_rule(arr)

    print(f"#{test_case} {base_arr.get_10_reverse()}")
