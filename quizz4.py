def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 1
    # Complete the while loop condition.
    while multiplier <= 5:

        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable

        #str(result)
        multiplier += 1


print(multiplication_table(3))

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15