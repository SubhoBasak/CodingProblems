def encode(txt):
    op_str = ''
    prv = txt[0]
    count = 1
    for i in txt[1:]:
        if i == prv:
            count += 1
        else:
            op_str += str(count)+prv
            count = 1
            prv = i
    op_str += str(count)+prv
    return op_str

def decode(txt):
    op_str = ''
    for i in range(0, len(txt), 2):
        j = txt[i]
        op_str += txt[i+1]*int(j)
    return op_str
