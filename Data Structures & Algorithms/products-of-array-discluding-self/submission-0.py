class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        suffix = []
        prefix = [] 
        for i in range(0,len(nums)):
            if i == 0:
                prefix.append(1)
                suffix.append(1)
            else:
                prefix.append(nums[i-1]*prefix[i-1])
                suffix.append(nums[len(nums)-i]*suffix[i-1])
        for i in range(0,len(nums)):
            product.append(prefix[i]*suffix[len(nums)-i-1])
        return product
        