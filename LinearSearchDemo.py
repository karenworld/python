def search_list(nums, target_num):
    """ Returns the index of TARGET_NUM in an unsorted list NUMS or -1 if not found.
    >>> search_list([3, 2, 1, 4], 3)
    2
    >>> search_list([14, 59, 99, 23, 37, 22], 23)
    3
    >>> search_list([14, 59, 99, 23, 37, 22], 47)
    -1
    """
    index = 1
    while index < len(nums):
        if nums[index] == target_num:
            return index
        index += 1
    return -1