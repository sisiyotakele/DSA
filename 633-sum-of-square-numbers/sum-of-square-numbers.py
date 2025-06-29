class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left =0
        right=int(c**0.5)
        while left<=right:
            curr_sum=left*left+right*right
            if curr_sum==c:
                return True
            elif curr_sum<c:
                left+=1
            else:
                right-=1
        return False


