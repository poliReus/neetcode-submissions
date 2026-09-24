class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #scorro l'array, se 7-nums[i] é nel set allora la coppia é fatta, altrimenti inserisco nel set nums[i]. Devo solo trovare il modo di recuperare l'indice, inserisco gli indici!
        sett = dict()
        res = list()
        for i in range(0,len(nums)):
            if target-nums[i] in sett:
                res = [sett[target-nums[i]],i]
            else:
                sett[nums[i]]=i
        return res

