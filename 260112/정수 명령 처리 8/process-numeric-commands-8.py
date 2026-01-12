N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
        else:
            self.tail = new_node
            
        self.head = new_node
        self.length += 1
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node  # 비어있던 경우

        self.head = new_node
        self.length += 1

    
    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.length += 1
    
    def pop_front(self):
        if self.head == None:
            print("Empty List")
        elif self.head.next == None:    # 원소가 하나
            print(self.head.data)
            self.head = None
            self.tail = None
        
            self.length = 0
        else:   # 일반적인 상황
            print(self.head.data)
            self.head.next.prev = None
            self.head = self.head.next

            self.length -= 1
    
    def pop_back(self):
        if self.tail == None:
            print("Empty List")
        elif self.tail.prev == None: # 원소가 하나
            print(self.tail.data)
            self.head = None
            self.tail = None

            self.length = 0
        else:   # 일반적인 상황
            print(self.tail.data)
            self.tail.prev.next = None
            self.tail = self.tail.prev

            self.length -= 1
    
    def size(self):
        return self.length
    
    def empty(self):
        return 1 if self.length == 0 else 0
    
    def front(self):
        print(self.head.data)
    
    def back(self):
        print(self.tail.data)

DLL = DoublyLinkedList()
for c, a in zip(command, A):
    if c == "push_front":
        DLL.push_front(a)
    elif c == "push_back":
        DLL.push_back(a)
    elif c == "pop_front":
        DLL.pop_front()
    elif c == "pop_back":
        DLL.pop_back()
    elif c == "size":
        DLL.size()
    elif c == "empty":
        DLL.empty()
    elif c == "front":
        DLL.front()
    elif c == "back":
        DLL.back()