def match_parentheses(st):
    lst = list(st)
    count = 0
    start = 0
    for i in lst:
        if i == '(':
            start += 1
            count += 1
        elif count == 0 or start == 0:
            count += 1
        elif start != 0:
            count -= 1
            start -= 1
    return count
