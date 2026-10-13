class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                count += 1

        if count > 0:
            return True
        else:
            return False
        