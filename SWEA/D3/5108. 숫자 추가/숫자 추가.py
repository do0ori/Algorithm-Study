class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, data=[]) -> None:
        self.head = Node()

        self.fill_initial_value(data)

    def fill_initial_value(self, data) -> None:
        if type(data) != list:
            data = [data]

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        for d in data:
            new_node = Node(d)
            last_node.next = new_node
            last_node = new_node

    def append(self, data) -> None:
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(data)

    def insert(self, index, data) -> None:
        prev_node = self.head
        i = 0
        while prev_node.next and i < index:
            prev_node = prev_node.next
            i += 1
        next_node = prev_node.next
        new_node = Node(data, next_node)
        prev_node.next = new_node

    def get(self, index):
        curr_node = self.head
        i = 0
        while curr_node.next and i <= index:
            curr_node = curr_node.next
            i += 1
        return curr_node.value

    def print_all(self) -> None:
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            print(curr_node.value, end=" ")
        print()


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = LinkedList(list(map(int, input().split())))
    numbers_to_add = [list(map(int, input().split())) for _ in range(M)]
    for index, number in numbers_to_add:
        arr.insert(index, number)

    print(f"#{test_case} {arr.get(L)}")
