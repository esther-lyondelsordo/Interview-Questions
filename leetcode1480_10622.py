# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        x = len(nums)
        sum = 0
        i = 0
        while i < x:
            if i == 0:
                runningSum.append(nums[i])
            else:
                sum += nums[i - 1]
                runningSum.append(sum + nums[i])
            i += 1

        return runningSum
