dic = {'2': ['a', 'b', 'c'],
       '3': ['d', 'e', 'f'],
       '4': ['g', 'h', 'i'],
       '5': ['j', 'k', 'l'],
       '6': ['m', 'n', 'o'],
       '7': ['p', 'q', 'r', 's'],
       '8': ['t', 'u', 'v'],
       '9': ['w', 'x', 'y', 'z']}

def decode_mapping(st):
    lst = list(st)
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        rest = []
    elif len(lst) > 1:
        rest = lst[1:]
    return __decode_mapping(lst[0], rest, '')

def __decode_mapping(cur, rest, st):
    lst = []
    for i in dic[cur]:
        if len(rest) == 1:
            x = __decode_mapping(rest[0], [], st+i)
            lst += x
        elif len(rest) == 0:
            lst.append(st+i)
        else:
            x = __decode_mapping(rest[0], rest[1:], st+i)
            lst += x
    return lst
