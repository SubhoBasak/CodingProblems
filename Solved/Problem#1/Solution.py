lst = input()
lst = lst.split(',')
lst = [int(i) for i in lst]

K = int(input())

size = len(lst)


for i in range(0, size-1):
    for j in range(i+1, size):
        if lst[i] + lst[j] == K:
            print(lst[i], lst[j])

