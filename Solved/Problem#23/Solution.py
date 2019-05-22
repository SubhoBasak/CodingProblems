def justify(arr, k):
    lst = [[]]
    cur_len = 0
    cur_set = 0
# first for loop devide the words in different sub-list (different lines)
# and the total length of those words is less than the k value
    for i in arr:
        lst[cur_set].append(i)
        cur_len += len(i)+len(lst[cur_set])-1
        if cur_len == k:
            lst.append([])
            cur_set += 1
            cur_len = 0
        elif cur_len > k:
            tmp = lst[cur_set].pop()
            lst.append([])
            cur_set += 1
            cur_len = 0
            lst[cur_set].append(tmp)
            cur_len += len(tmp)

# In this second for loop each sub-list is taken and with the inner for loops
# the length of the words in each sub-list is calculated before the while loop
# started and also in every cycle of the while loop so that the while loop,
# which add space time to time in each words in sub-list to maintain every
# lines length, can not add more spaces between the words
    for i, arr in enumerate(lst):
        ln = 0
        indx = 0
        for j in arr:
            ln += len(j)
        while ln != k:
            arr[indx] += ' '
            indx += 1
            if indx >= len(arr)-1:
                indx = 0
            ln = 0
            for j in arr:
                ln += len(j)
        lst[i] = arr

# Finally, this for loop takes each sub-list for the list and join them to
# make a string and the insert it to it's index in the list
    for i, arr in enumerate(lst):
        tmp = ''
        for j in arr:
            tmp += j
        lst[i] = tmp


    for i in lst:
        print(i)


# I know that there is lot of errors and I will try to improve the code as
# soon as possible
