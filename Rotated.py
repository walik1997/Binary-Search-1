class Solution:
    def search(self, nums: list[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while low <= high: 
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <=target <= nums[mid]:
                    high = mid - 1    
                else:
                    low = mid+1
            else:
                if nums[mid]< target <= nums[high]:
                    low = mid + 1
                else:
                     high=mid-1    
        return -1
a=Solution()
b=a.search([3,4,5,6,0,1,2],target=2)
print(b)