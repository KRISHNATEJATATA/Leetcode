class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[None]*n
        for i in range(n):
            arr[i]=i+1
        i=0
        for j in range(n-1):
            for a in range(k-1):
                i=(i+1)%n
            arr.remove(arr[i])
            n-=1
        return arr[0]
