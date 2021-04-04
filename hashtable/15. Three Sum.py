# Solution I: two pointers
# The hard part is to avoid duplicate.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = []
        nums.sort()
        for i in range(N-2):
            # This is the first device to avoid duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i] * (-1)
            left = i+1
            right = N-1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # This is the second device to avoid duplicate. It only controls the left duplicate.
                    # The right side duplicate will not occur if the left duplicate is handled.
                    # For example, target = 3, range is [1,1,2,2,2]. left = 0, right = 4. 
                    # next left non-duplicate is left = 2, right has to move in this case.
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return result

# Solution II: hashtable
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # set as result can avoid duplicate
        result = set()
        nums.sort()
        
        for i in range(len(nums)-2):
            # Avoid duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i] * (-1)
            # below is a two sum problem
            h = {}
            for v in nums[i+1:]:
                if target - v in h:
                    # make sure what is stored in h
                    result.add((-target, target-v, v))
                else:
                    h[v] = 1
        return list(result)