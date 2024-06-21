class Solution:
    def search(self, reader, target):
        low = 0
        high=1
        while target > reader.get(high):
            low=high
            high= high*2
        while low <=high:
            mid=low+(high-low)//2
            if target==reader.get(mid):
                return mid
            if target>reader.get(mid):
                low=mid+1
            else:
                high=mid-1
                        
        return -1