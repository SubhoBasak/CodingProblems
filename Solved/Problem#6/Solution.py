s = input()

dct = {}

def num_ways(data):
    if len(data) == 1:
        print('*')
        return 1
    elif len(data) == 2:
        if int(data) in range(27):
            print('**')
            return 2
        return 1
    elif data in dct:
        return dct[data]
    else:
        left = num_ways(data[1:])
        if int(data[0:2]) in range(27):
            right = num_ways(data[2:])
            dct[data] = left+right
            return left+right
        return left

print(num_ways(s))

