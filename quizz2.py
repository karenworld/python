#Question 4

#Write a function that takes an argument n and returns the sum of integers from 1 to n.
#For example, if n=5, your function should add up 1+2+3+4+5 and return 15.
# If n is less than 1,
#just return 0. Use a while loop to calculate this sum.

def sum_of_integers(n):
    if n < 1:
        return 0

    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i = i + 1


    return sum


print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15