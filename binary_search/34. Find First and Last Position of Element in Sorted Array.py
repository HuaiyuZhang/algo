class Solution:
    def find_start(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1
    def find_end(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l+1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return r  if nums[r] == target else -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        return ([self.find_start(nums, target), self.find_end(nums, target)])
        