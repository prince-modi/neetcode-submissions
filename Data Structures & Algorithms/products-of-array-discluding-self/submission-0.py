class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [m,n,o,p]
        # [nop,mop,mnp,mno]

        # [1,m,mn,mno]
        # [nop,op,p,1]
        # [nop,mop,mnp,mno]

        prefix_prod = [1]
        suffix_prod = [1]
        for num in nums:
            prefix_prod.append(prefix_prod[-1]*num)
        for num in nums[::-1]:
            suffix_prod.append(suffix_prod[-1]*num)
        return [i*j for i,j in zip(prefix_prod[:-1],suffix_prod[::-1][1:])]
        