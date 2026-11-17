class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longitud=0
        nums=set(nums)
        for n in nums:
            if (n-1) not in nums:
                dim_cad=0
                while (n+dim_cad) in nums:
                    dim_cad+=1
                longitud=max(longitud,dim_cad)
        return longitud

        