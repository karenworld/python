# Let's try. Consider all two-digit integers that are divisible by 7:
# 14,21,28,35,49,56,63,70,77,84,91,98

# We know that dividing the required integer by should result in a single digit integer.
# This allows us to rule out all numbers starting from the list.
# We can then check manually that out of the remaining numbers the only one satisfying the required property is



# The argument above is simple, but still some reasoning is needed.
# One could use a brute force search instead.

for n in range(10, 100):
    if n == 7 * int(str(n)[1:]):
        print(n)

# This code goes through all integers in the range [10,99]
# In general, rang(a,b) where a<=b are integers, denotes a list that contains a, a+1,.....,b-1(empty if a =b ).
# To remove the first digit of a number, we convert it to a string (by calling the str() function),
# then use slicing ([1:]) to remove the first symbol of the resulting string,
# and finally convert the resulting string back to an integer.