def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [1, 2, 3, 4, 5]
print(array_sum(arr))