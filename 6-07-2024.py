class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pas=1
        pos=0
        for i in range(time):
            if pas==1:
                pos+=1
                if pos==n-1:
                    pas=0
            else:
                pos-=1
                if pos==0:
                    pas=1
        return pos+1
