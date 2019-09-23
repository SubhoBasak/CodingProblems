# Solution part

def __change_color(mat, x, y, cur_c, c):
        try:
            if mat[y][x] == cur_c:
                change_color(mat, x, y, c)
        except IndexError:
            return None

def change_color(mat, x, y, c):
    cur_c = mat[y][x]
    mat[y][x] = c
    __change_color(mat, x-1, y, cur_c, c)
    __change_color(mat, x+1, y, cur_c, c)
    __change_color(mat, x, y-1, cur_c, c)
    __change_color(mat, x, y+1, cur_c, c)

# Testing part

mat = [['B', 'B', 'W'],
       ['W', 'W', 'W'],
       ['W', 'W', 'W'],
       ['B', 'B', 'B']]

print('before changing color')
for i in mat:
    print(i)

change_color(mat, 2, 2, 'G')

print('\n\nafter changin color')
for i in mat:
    print(i)
