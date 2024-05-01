def search_list(nums, target_num):
    """ Returns the index of TARGET_NUM in sorted list NUMS or -1 if not found.
    >>> search_list([1, 2, 3, 4], 3)
    2
    >>> search_list([14, 23, 37, 48, 59], 23)
    1
    >>> search_list([14, 23, 37, 48, 59], 47)
    -1
    """
    min_index = 1
    max_index = len(nums)
    while min_index <= max_index:
        middle_index = (min_index + max_index) // 2
        if target_num == nums[middle_index]:
            return middle_index
        elif target_num > nums[middle_index]:
            min_index = middle_index + 1
        else:
            max_index = middle_index - 1
    return -1

print(search_list([14, 23, 37, 48, 59], 23))