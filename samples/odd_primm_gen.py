def odd_gen(start, stop):
    while start < stop:
        if start % 2 != 0:
            yield start
        start += 1
