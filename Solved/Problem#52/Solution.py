def perfect_number(num):
    num = list(str(num))
    num_2 = ''
    for i in range(len(num)):
        num[i] = int(num[i])
        num_2 += str(num[i])
    sub_sum = sum(num)
    if sub_sum >= 10:
        return None
    return int(num_2 + str(10-sub_sum))
