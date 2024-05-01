def is_prime(n):
    #  from 2 because 1 and any number less than 1 cannot be prime.
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(40))


# Growth of Time
# Linear.
#
# Explanation:
# In the worst case, n is prime, and we have to execute the loop n - 2 times.
# Each iteration takes constant time (one conditional check and one return statement).
# Therefore, the total time is (n - 2) x constant, or simply linear.
