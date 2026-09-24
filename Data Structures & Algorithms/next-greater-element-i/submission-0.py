class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=0
        res = []
        for i in range(0,len(nums1)):
            interaction = 0
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j]:
                    for k in range(j,len(nums2)):
                        if nums1[i]<nums2[k]:
                            res.append(nums2[k])
                            interaction=interaction +1
                            break
            if interaction==0:
                res.append(-1)
        return res
                
        