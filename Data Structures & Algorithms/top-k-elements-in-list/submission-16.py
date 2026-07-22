class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        counter = [[] for _ in range(len(nums) + 1)]

        for num, count in hashmap.items():
            counter[count].append(num)
        
        res = []
        for i in range(len(counter)-1, -1, -1):
            for num in counter[i]:
                res.append(num)
                if len(res) == k:
                    return res