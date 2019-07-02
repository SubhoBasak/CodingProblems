def max_mul(lst):
    mx = lst[0]*lst[1]*lst[2]
    for i, x in enumerate(lst):
        for j, y in enumerate(lst):
            if i == j:
                continue
            for k, z in enumerate(lst):
                if j == k or i == k:
                    continue
                if x*y*z > mx:
                    mx = x*y*z
    return mx
