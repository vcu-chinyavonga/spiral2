def spiralize(size, n=1):
    n = 1
    count = 0
    gap = 2
    total = 0

    while n <= size ** 2:
        total += n
        n += gap
        count += 1
        if count == 4:
            gap += 2
            count = 0

    return total
    

