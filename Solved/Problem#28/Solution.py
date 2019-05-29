def segregate(seq):
    i = 0
    j = 0
    while i < len(seq):
        if seq[i] == 'R':
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            j += 1
        i += 1
    i = j
    while i < len(seq):
        if seq[i] == 'G':
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            j += 1
        i += 1
    i = j
    while i < len(seq):
        if seq[i] == 'B':
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            j += 1
        i += 1
    return seq
