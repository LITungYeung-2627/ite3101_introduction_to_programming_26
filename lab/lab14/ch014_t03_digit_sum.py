def digit_sum(n:int) -> int:
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return total