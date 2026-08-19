class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        store = []
        counter = Counter(nums)

        for num, count in counter.items():
            store.append([count, num])
        store.sort()

        for i in range(len(store)-1, -1, -1):
            res.append(store[i][1])
            if len(res) == k:
                return res            