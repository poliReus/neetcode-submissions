class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #scorro l'array, se 7-nums[i] é nel set allora la coppia é fatta, altrimenti inserisco nel set nums[i]. Devo solo trovare il modo di recuperare l'indice, inserisco gli indici!
        sett = dict()
        res = list()
        for i in range(0,len(nums)):
            if target-nums[i] in sett.values():
                dict_invertito = {v: k for k, v in sett.items()}
                #print(dict_invertito[target - nums[i]])
                res = [dict_invertito[target-nums[i]],i]
            else:
                #print(sett)
                sett[i]=nums[i]
        return res

