#Write a function to find the longest common prefix string amongst an array of strings.
from itertools import count

nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def array_sorting(nums):
    numset = set(sorted(nums))
    return print(f"{len(numset)}, nums = {numset}")

print(array_sorting([1,1,2]))