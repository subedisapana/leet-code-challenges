def is_harshad_number(x):
    sum_of_digits = sum(int(digit) for digit in str(x))
    if x % sum_of_digits == 0:
        return sum_of_digits
    else:
        return -1

# Test cases
print(is_harshad_number(18))  # Output: 9
print(is_harshad_number(23))  # Output: -1
