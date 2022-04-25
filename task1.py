

# 1. Removing duplicates from a list using set
# 2. Making a list of unique elements
# 3. Merge sets if one or more elements are common


# 1. Removing duplicates from a list using set
a = [1,2,3,3,3,3,4,5,5,5,5]
set1 = set([1,2,3,3,3,3,4,5,5,5,5])
print(set1)
s = list(set1)
print(s)  #output in list

# 2. Making a list of unique elements

# 3. Merge sets if one or more elements are common
set2 = {1,2,3,4,5}
set3 = {4,5,6,7,8,9}

# s = ['Hello', 'world']
# listtoStr1 = s.join(",")
# print(listtoStr1)

# listToStr = ' '.join([str(elem) for elem in s])
#
# print(listToStr)

My_list = ['a'] * 1000
print(My_list)
print(','.join(My_list))

