class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic=defaultdict(int)
        for i in arr1:
            dic[i]+=1
        arr=[]
        for i in arr2:
            for j in range(dic[i]):
                arr.append(i)
                arr1.remove(i)
        return arr+sorted(arr1)