def biography_list(people) :
    # Iterate over each "person" in the given "people" list of tuples.

    for person in people :

        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"
        name = person[0]
        age = person[1]
        profession = person[2]
        # Format the required sentence and place the 3 variables
        # in the correct placeholders using the .format() method.
        print ( "{} is {} years old and works as a {}".format ( name , age , profession ) )
      # Call to the function:


biography_list ( [("Ira" , 30 , "a Chef") , ("Raj" , 35 , "a Lawyer") , ("Maria" , 25 , "an Engineer")] )

# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer
