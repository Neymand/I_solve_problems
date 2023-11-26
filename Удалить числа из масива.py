nums = [3, 2, 2, 3]
len1 = len(nums)
val = 3

nums[:] = (x for x in nums if x != val)
val = len(nums)
dif = len1 - val

nums[val:] = '_' * dif

print(nums)

a = [0, 1, 3, 0, 4,'_','_','_']