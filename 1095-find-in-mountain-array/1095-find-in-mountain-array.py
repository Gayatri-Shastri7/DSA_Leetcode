# Logic:
# arr=[1,2,3,4,5,3,1]
# Target = 3
# Find peak element -> 4 index
# Binary Search in asc array -> (0,4)
# If not found, binary search in



# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

'''
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def search(self,mountain_arr: 'MountainArray')-> bool:
            peek = peakIndexInMountainArray(arr)
            firstTry= binarySearch(arr,target,0,peak)
            if(firstTry!= -1):
                return firstTry
            return binarSearch(arr, target, peak+1, len(arr)-1)
        
        def peakIndexInMountainArray(self, arr: List[int]) -> int:
            n = len(arr)
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if (arr[mid]>arr[mid+1]):
                    right = mid
                else:
                    left = mid + 1
            return left    
    
        def binarySearch(arr,x, start,end):
            isAsc = arr[start] < arr[end]
            if (end >= start):
                middle = (int)(start + (end - start) / 2)

                # If the element is present
                # at the middle itself
                if (arr[middle] == x):
                    return middle

                if (isAsc == True):

                    # If element is smaller than mid,
                    # then it can only be
                    # present in left subarray
                    if (arr[middle] > x):
                        return binarySearch(
                            arr, start,
                            middle - 1, x)

                    # Else the element can only be present
                    # in right subarray
                    return binarySearch(arr, middle + 1,
                                        end, x)

                else:
                    if (arr[middle] < x):
                        return binarySearch(arr, start,middle - 1, x)

                    # Else the element can only be present
                    # in left subarray
                    return binarySearch(arr, middle + 1,end, x)
            # Element not found
            return -1

'''          
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.find_peak(mountain_arr)
        if mountain_arr.get(peak) == target:
            return peak
        ret = self.binary_search(target, mountain_arr, 0, peak + 1, True)
        if ret != -1:
            return ret
        return self.binary_search(target, mountain_arr, peak, mountain_arr.length(), False)
        
    def find_peak(self, mountain_arr: 'MountainArray'):
        l = 0
        r = mountain_arr.length()
        while l < r:
            mid = (l + r) // 2
            if 0 < mid < mountain_arr.length():
                if mountain_arr.get(mid + 1) > mountain_arr.get(mid):
                    l = mid
                elif mountain_arr.get(mid) < mountain_arr.get(mid - 1):
                    r = mid + 1
                else:
                    return mid
                    
    
    def binary_search(self, target: int, mountain_arr: 'MountainArray', l, r, asc):
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < target:
                if asc:
                    l = mid + 1 
                else:
                    r = mid
            elif mountain_arr.get(mid) > target:
                if asc:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target == mountain_arr.get(mid):
                    return mid
                else:
                    break
        return -1
