N = int(input())

da = []
for _ in range(N):
    i = input().split()
    command = i[0]
    if command == 'push_back':
        da.append(int(i[1]))
    elif command == 'pop_back':
        da.pop()
    elif command == 'size':
        print(len(da))
    elif command == 'get':
        print(da[int(i[1])-1])
    else:
        print("error")
