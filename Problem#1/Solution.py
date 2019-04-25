lst = input('\nEnter the list numbers seperated with a comma. \nFor example - 1,2,3,4,5.\n\nInput values : ')
lst = lst.split(',')
lst = [int(i) for i in lst]

K = int(input('Enter the value of K : '))

size = len(lst)


for i in range(0, size-1):
    for j in range(i+1, size):
        if lst[i] + lst[j] == K:
            print('Combinations#')
            print('First number is : ', lst[i])
            print('Second number is : ', lst[j])

