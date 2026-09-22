class Solution:
    def hasDuplicate(self, nums: List[int]) ->  bool:
        arr = {""}
        for i in nums:
            if i not in arr:
                arr.add(i)
            else:
                return True
        return False