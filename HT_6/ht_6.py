def group_of_values(numbers_group, n):
    for value  in numbers_group:
        if n == value:
            return True
        return False
    print(group_of_values([1, 5, 8, 3], 3))
    print(group_of_values([1, 5, 8, 3], -1))