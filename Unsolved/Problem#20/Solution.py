row = int(input())
mat = []
for i in range(row):
    mat.append([bool(int(j)) for j in input().split()])

start = [int(i) for i in input().split()]
stop = [int(i) for i in input().split()]

while True:
    
