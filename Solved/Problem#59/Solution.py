def divide(m, n):
    count = 0
    total = 0
    while total+n <= m:
        total += n
        count += 1
    return count
