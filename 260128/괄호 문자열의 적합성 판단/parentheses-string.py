str = input()

# Please write your code here.
stack = []
status = "Yes"
for s in str:
    if s == "(":
        stack.append(s)
    else:
        if not stack:
            status = "No"
            break;
        else:
            stack.pop()
    
if stack:
    status = "No"

print(status)