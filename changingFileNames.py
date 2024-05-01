filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        new = filename.replace(".hpp", ".h")
        new_filenames.append(new)
    else:
        new_filenames.append(filename)



print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]