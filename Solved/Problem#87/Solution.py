def reverse_32bit_int(bits):
    bits = str(bits)
    r_bits = bits[::-1]
    print(r_bits)
    cur_val = 1
    cur_sum = 0
    for i in r_bits:
        if i == '1':
            cur_sum += cur_val
        cur_val *= 2
    return bin(cur_sum)

