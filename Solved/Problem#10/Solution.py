s = input()
qry = input()
qry = qry.split(',')

op = []

for i in qry:
    if i.startswith(s):
        op.append(i)

print(op)
