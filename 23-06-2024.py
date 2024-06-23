from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()  # Increasing monotonic queue
        dec = deque()  # Decreasing monotonic queue
        
        res = 0
        left = 0
        
        for right in range(len(nums)):
            # Maintain increasing order in inc
            while inc and inc[-1] > nums[right]:
                inc.pop()
            
            # Maintain decreasing order in dec
            while dec and dec[-1] < nums[right]:
                dec.pop()
            
            # Add current element to both deques
            inc.append(nums[right])
            dec.append(nums[right])
            
            # Check if the current window is valid
            while dec[0] - inc[0] > limit:
                # Remove the element going out of the window
                if dec[0] == nums[left]:
                    dec.popleft()
                if inc[0] == nums[left]:
                    inc.popleft()
                left += 1  # Slide the window
            
            # Update the result with the maximum window size
            res = max(res, right - left + 1)
        
        return res