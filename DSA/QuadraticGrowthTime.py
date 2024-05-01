def linear_sort(nums):
    """Performs an in-place sorting of NUMS.
    >>> l = [2, 3, 1, 4]
    >>> linear_sort(l)
    >>> l
    [1, 2, 3, 4]
    """
    i = 0
    while i < len(nums):
        min_index = i
        j = i + 1
        # Find next smallest value
        while j < len(nums):
            if nums[j] < nums[min_index]:
                min_index = j
            j += 1
        # Swap if new minimum found
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
        i += 1