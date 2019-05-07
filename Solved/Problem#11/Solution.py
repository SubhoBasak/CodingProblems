k = int(input())
s = input()

for i, j in enumerate(s):
    op = ''
    if i >= k-1:
        for m in range(k-1):
            if s[i-(1+m)] == s[i+(1+m)]:
                op += s[i-(m+1)]
            else:
                op = ''
                break
        if op == '':
            continue
        if len(op) == k-1:
            x = ''
            lst = list(op)
            lst.reverse()
            for p in lst:
                x += p
            op = x+s[i]+op
            break

print(op)
