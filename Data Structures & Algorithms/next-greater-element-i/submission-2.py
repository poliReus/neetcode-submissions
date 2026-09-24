class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        maxss = {}
        stack = [] 
        
        
        for i in range(len(nums2) - 1, -1, -1):
            curr = nums2[i]
            while stack and stack[-1] <= curr:
                stack.pop()
            
            if stack:
                maxss[curr] = stack[-1]
            else:
                maxss[curr] = -1
            stack.append(curr)
        ris = []
        for num in nums1:
            ris.append(maxss[num])
            
        return ris