def pascal(c, r):
    result = 1  # The value at row 0, column 0 is 1
    for i in range(c):
        result = result * (r - i) // (i + 1)
    return result

# Test cases
print(f'pascal(0,2) = {pascal(0,2)}')  # Should return 1
print(f'pascal(1,2) = {pascal(1,2)}')  # Should return 2
print(f'pascal(1,3) = {pascal(1,3)}')  # Should return 3
print(f'pascal(1,4) = {pascal(1,4)}')  # Should return 4
print(f'pascal(1,5) = {pascal(1,5)}')  # Should return 5
print(f'pascal(2,5) = {pascal(2,5)}')  # Should return 10
print(f'pascal(2,4) = {pascal(2,4)}')  # Should return 6
print(f'pascal(10,2) = {pascal(2,10)}')  # Should return 45