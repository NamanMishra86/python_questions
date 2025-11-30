def Secound_largest_value(nums):
    numsc=list(set(nums))
    nums.sort()
    return nums[-2]
print(Secound_largest_value([10,20,30,40,50,60]))