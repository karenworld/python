def outer_function() :
    num = 20

    def inner_function() :
        global num
        num = 25

    print ( "Before calling inner_function(): " , num )
    inner_function ()
    print ( "After calling inner_function(): " , num )


outer_function ()
# print ( "Outside both function: " , num )
# Before calling inner_function():  20
# After calling inner_function():  20
# Outside both function:  25