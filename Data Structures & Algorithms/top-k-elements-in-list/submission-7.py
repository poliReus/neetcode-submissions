class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mappa = dict()
        for i in range(0, len(nums)):
            if nums[i] not in mappa:
                mappa[nums[i]] = 1 
            else:
                mappa[nums[i]] = mappa[nums[i]] + 1
        heap=[]
        for i,j in mappa.items():
            heapq.heappush(heap, (-j,i))
        ris = []
        for i in range(0, k):
            ris.append(heapq.heappop(heap)[1])
        return ris
        