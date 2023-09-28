nums = {1, 2, 3, 4} #no duplicates allowed and no index

nums2 = set((1,2,3,4,5,6))

print(nums)
print(nums2)

nums3 = {1, 2, 2, 3, 3, 3, 4}
print(nums3)

nums = {1, True, 2, False, 3, 4, 0} # false is 0 and true is 1

print(nums) #get sorted

print(2 in nums)

nums.add(5)

print(nums)

otherNums = {6, 7, 8}

nums.update(otherNums) #work with tuples, lists or dictionaries too

print(nums)

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two) #keep the duplicates only

print(one)

one = {1, 2, 3}

one.symmetric_difference_update(two) # exclude the duplicates

print(one)
