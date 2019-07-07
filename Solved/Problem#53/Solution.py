def count_in_mat(n, k):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j == k:
                count += 1
    return count
