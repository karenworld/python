def bonk(n):
    sum = 0
    while n >= 2:
        sum += n
        n = n / 2
    return sum

# Logarithmic.

# Explanation: As we increase the value of n, the amount of time needed to evaluate a call to bonk scales logarithmically.
# Let's use the number of iterations of our while loop to illustrate an example.
# When n = 1, our loop iterates 0 times. When n = 2, our loop iterates 1 time.
# When n = 4, we have 2 iterations.
# And when n = 8, a call to bonk(8) results in 3 iterations of this while loop.
# As the value of the input scales by a factor of 2, the number of iterations increases by 1.
# This indicates that this function runtime has a logarithmic order of growth.
