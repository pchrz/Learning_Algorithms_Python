#/usr/bin/python3

### Leetcode problem:
##### https://leetcode.com/problems/two-sum/

nums = [3,2,4]
target = 6

#nums = [2,7,11,15]
#target = 9


### My first attempt, double for loop. 
### Is an uneligent brute force solution running O(n^2)
# def twoSum(nums, target):
#    for x in range(len(nums)):
#        for y in range(x+1, len(nums)):
#            sum = nums[x] + nums[y]
#            if target == sum:
#                return [x, y]
#
### RESULTS ###
## Success
## Runtime: 7460 ms, faster than 5.53% of Python3 online submissions for Two Sum.
## Memory Usage: 14.8 MB, less than 95.39% of Python3 online submissions for Two Sum.

### More efficient option, compliment sum.
### Due to one for loop it will run at O(n)
def twoSum(nums, target):
    complementMap = dict()
    
    for idx in range(len(nums)):
        num = nums[idx] #3, 2, 4
        comp = target - num #3, 4, 2
        if num in complementMap:
            return [complementMap[num], idx]
        else:
            complementMap[comp] = idx  #{3,0}, {4, 1}, {2,2}     

### RESULTS ###
## Success
## Runtime: 136 ms, faster than 38.41% of Python3 online submissions for Two Sum.
## Memory Usage: 15.4 MB, less than 14.26% of Python3 online submissions for Two Sum.

print(twoSum(nums, target))


