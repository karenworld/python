# Problem. Does there exist a six-digit number that starts with 100 and is a multiple of 9127?


for i in range(100000, 101000):
    if i % 9127 == 0:
        print(i)

        # 100397