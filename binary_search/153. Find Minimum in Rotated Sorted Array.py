# solution 1
def findMin(self, nums: List[int]) -> int:
    if nums[-1] >= nums[0]:
        return nums[0]
    else:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if (nums[mid] > nums[mid + 1]):
                return nums[mid + 1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1

# solution 2
def findMin(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]

# solution 3 recursion
def findMin(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return None
    if len(nums)<= 2:
        return min(nums)
    else:
        mid = len(nums)//2
        if nums[mid] > nums[-1]:
            return self.findMin(nums[mid:])
        else:
            return self.findMin(nums[:mid+1])