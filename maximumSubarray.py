#CHALLENGE:
#===================================================================================
#Given an integer array nums, find the contiguous subarray (containing at least one 
#number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.
#===================================================================================

nums = [1, -5, 12, 3, -7, -6, -2]

top_sum, pres_sum = nums[0], nums[0] #top_sum is going to keep track of the largest sum so far
for i in range (1, len(nums)):       #while pres_sum... the logic behind pres_sum is difficult to understand
    
    print (i, nums[i], pres_sum, top_sum)
    pres_sum = max (nums[i], pres_sum+nums[i]) #pres sum updates to the larger of two values: either the current value (num[i]) or the present sum + the current value
    top_sum = max(pres_sum, top_sum) #top_sum updates to max value of pres_sum, top_sum

print (top_sum)

#learned about the max function