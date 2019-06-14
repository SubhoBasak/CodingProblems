def max_contigious_subset_val(lst):
    cur_max = glb_max = lst[0]
    for i in lst[1:]:
        cur_max = max(i, cur_max+i)
        if cur_max > glb_max:
            glb_max = cur_max
    if glb_max < 0:
        glb_max = 0
    return glb_max
