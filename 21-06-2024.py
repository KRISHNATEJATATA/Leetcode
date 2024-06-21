class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        max_window=window=0
        base_case=0
        for i in range(len(customers)):
            if grumpy[i]:
                window+=customers[i]
            else:
                base_case+=customers[i]
            if i-l+1>minutes:
                if grumpy[l]:
                    window-=customers[l]
                l+=1
            max_window=max(max_window,window)
        return max_window+base_case