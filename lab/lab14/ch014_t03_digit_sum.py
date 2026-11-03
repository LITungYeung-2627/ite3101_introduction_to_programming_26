def digitsum(n:int):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total