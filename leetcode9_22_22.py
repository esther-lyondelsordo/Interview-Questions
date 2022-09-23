class Solution27:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_vals = 0
        # count the instances of val
        for i in range(len(nums)):
            if nums[i] == val:
                num_vals += 1
        # remove val
        while num_vals > 0:
            nums.remove(val)
            num_vals -= 1


class Solution416:
    def canPartition(self, nums: List[int]) -> bool:
        big_sum = sum(nums)

        # the sum of nums must be even
        if big_sum % 2 == 1:
            return False

        """
        we can't have one element that is greater 
        than the sum of the rest of the elements
        """
        for i, val in enumerate(nums):
            index = val
            if val > sum(nums[0:i] + nums[i + 2 :]):
                return False

        # TODO: Solution is incomplete
