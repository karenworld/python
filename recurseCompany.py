def count_users(group) :
    count = 0
    # for member in  group  :
    #     count += 1
    #     if member  :
    count += count_users ( group )
# return count


print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18




