def longest_path(st):
    st = st.split('\n')
    return __longest_path(st[1:], 1, st[0])

def __longest_path(dirs, level, cur):
    if len(dirs) == 0:
        return None

    tmp = '' # store the file path to return it later
    arr = []
    for i in dirs:
        if i.count('\t') == level:
            arr.append([])
            
    cur_indx = -1
    for i in dirs:
        if i.count('\t') == level:
            cur_indx += 1
            arr[cur_indx].append(i)
        elif i.count('\t') > level:
            arr[cur_indx].append(i)
        if '.' in i and i.count('\t') == level:
            if len(tmp) == 0:
                tmp = cur+'/'+i.strip('\t')
            elif len(cur+'/'+i) > len(tmp):
                tmp = cur+'/'+i.strip('\t')
    level += 1
    for i in range(len(arr)):
        x = __longest_path(arr[i][1:], level, '/'.join([cur, arr[i][0].strip('\t')]))
        if x != None:
            tmp = max(x, tmp)
    return tmp

# testing part

st = 'dir\n\tsubdir1\n\t\tsubsubdir1\n\t\tsubsubdir2\n\t\t\tfile3.txt\n\t\tfile2.txt\n\tsubdir2\n\t\tsubsubdir3\n\tfile1.txt'
print(st)
print('Longest path : ', longest_path(st))
