class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {_:[] for _ in range(len(nums) +1)}
        buckets[0] = set(nums)
        for n in nums:
            for i, b in buckets.items():
                if n in b:
                    b.remove(n)
                    buckets.get(i+1).append(n)
                    break
        ans = []
        for i in range(len(nums), 0, -1):
            if len(ans) < k and len(buckets[i]) > 0:
                ans += buckets[i]
        return ans     