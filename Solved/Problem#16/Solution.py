lst = input().split(',')
lst = [int(i) for i in lst]
k = int(input())

for i in range(len(lst)-(k-1)):
    lst[i] = max(lst[i:i+k])
for i in range(k-1):
    lst.pop()

print(lst)
