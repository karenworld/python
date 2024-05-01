def foo(lst, i):
    mid = len(lst) // 2
    if mid == 0:
        return lst
    elif i > 0:
        return foo(lst[mid:], -1)
    else:
        return foo(lst[:mid], 1)
    # Logarithmic Θ(log(n)).
    # A single recursive call is made in the body of foo on half the input list
    # (either the first half or the second half depending on the input flag i).
    # The base case is executed when the list either is empty or has only one element.
    # We start with an n element list and halve the list until there is at most 1 element,
    # which means there will be log(n) total calls.
    # Each call, constant work is done if we ignore the recursive call.
    # The total runtime is then log(n) * θ(1).