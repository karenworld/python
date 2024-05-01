# Does there exists 3 digits and remainder 1 when divided by 2,3,4,5,6,7 ?
# Again, we can write a simple program which checks all three-digit numbers.


# Python all() method is a built-in function that returns TRUE if all of the items of a passed iterable (List, Dictionary, Tuple, Set, etc.) are True;
# otherwise, it returns FALSE.
for n in range(100, 1000):
    if all(n % m == 1 for m in range(2, 8)):
        print(n)
