"""
Find Minimum in Rotated Sorted Array
Problem: LeetCode 153 - Find Minimum in Rotated Sorted Array
Difficulty: Medium

problem statement:

You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. 
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # if the mid element is greater than the right element, then the minimum element is on the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            # else min element is on the left side or equal to mid
            else:
                right = mid
        # if num[left] == nums[right] then we have found the minimum element
        return nums[left]

# Time Complexity: O(log n)
# Space Complexity: O(1)
if __name__ == "__main__":
    nums = [3,4,5,6,1,2]
    s = Solution()
    print(s.findMin(nums))      
        