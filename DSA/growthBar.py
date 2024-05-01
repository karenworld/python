def bar(n):
    i, sum = 1, 0
    while i <= n:
        sum += biz(n)
        i += 1
    return sum

def biz(n):
    i, sum = 1, 0
    while i <= n:
        sum += i**3
        i += 1
    return sum

# To analyze the time complexity of the provided code, let's look at each function individually:
#
#     biz(n):
#         This function contains a loop that iterates from 1 to n.
#         Inside the loop, it performs a constant number of operations
#         (raising i to the power of 3 and adding it to sum).
#         The loop runs n times.
#         Therefore, the time complexity of this function is O(n).
#
#     bar(n):
#         This function also contains a loop that iterates from 1 to n.
#         Inside the loop, it calls the biz(n) function,
#         which has a time complexity of O(n).
#         Therefore, for each iteration of the loop in bar(n), the time complexity is O(n).
#         Since there's another loop that runs n times (from 1 to n),
#         and each iteration of this loop has a time complexity of O(n),
#         the overall time complexity of bar(n) is O(n^2).
#
# In summary:
#
#     The biz(n) function has a time complexity of O(n).
#     The bar(n) function has a time complexity of O(n^2) due to the nested loop and the call to biz(n) within each iteration of the outer loop.
# The time complexity of bar(n) is O(n^2).
#
# In terms of growth rate, it indicates a quadratic time complexity. Quadratic time complexity means that as the input size (n) increases, the time taken by the algorithm grows quadratically, i.e., proportional to the square of the input size.
#

# This type of growth is often seen in algorithms that have nested loops where each loop iterates over the size of the input.

#
# Quadratic.
#
# Explanation: The body of the while loop in bar is executed n times.
# Each iteration, one call to biz(n) is made. Note that n never changes,
# so this call takes the same time to run each iteration.
# Taking a look at biz, we see that there is another while loop.
#     Be careful to note that although the term being added to sum is cubed (i**3),
#     i itself is only incremented by 1 in each iteration.
#     This tells us that this while loop also executes n times,
#     with each iteration taking constant time, so the total time of biz(n) is n x constant,
#     or linear. Knowing that each call to biz(n) takes linear time, we can conclude that each
#     iteration of the while loop in bar is linear. Therefore, the total runtime of bar(n) is
#     quadratic.

