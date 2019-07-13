def find_possible_steps(n, m):
    if n == 1:
        return 1
    elif m == 1:
        return 1
    elif n == 2:
        return m
    elif m == 2:
        return n
    elif n == m:
        x = find_possible_steps(n-1, m)
        return 2*x
    else:
        x = find_possible_steps(n-1, m)
        y = find_possible_steps(n, m-1)
        return x+y
