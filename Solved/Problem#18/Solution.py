d = input().split(',')
d = list(map(lambda x: x.strip(), d))
string = input()

def extract(st, prv, dct):
    for i, j in enumerate(dct):
        if st.startswith(j):
            if prv == None:
                cpy = [j]
            else:
                cpy = prv + [j]
            extract(st[len(j):], cpy, dct[:i]+dct[i+1:])
    if len(st) == 0:
        print(prv)

extract(string, None, d)
