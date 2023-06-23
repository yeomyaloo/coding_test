# stack이 있나 확인하고 해당 값이 다음 값보다 크면 넣고 작으면 뺴고

n, k = map(int,input().split())
li = list(input())
stack = []

for i in li:
    while stack and stack[-1] < i and k > 0:
        stack.pop()
        k -= 1
    stack.append(i)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))