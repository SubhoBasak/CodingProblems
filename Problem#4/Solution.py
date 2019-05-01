lst = input()
lst = lst.split(',')
lst = [int(i) for i in lst]

x = 1

while True:
    if x in lst:
        x += 1
    else:
        print(x)
        break
