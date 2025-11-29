import heapq
from collections import Counter


class Solution:

    def reorganizeString(self, s: str) -> str:
        n = len(s)
        cnt = Counter(s)
        # quick impossibility check
        if any(v > (n + 1) // 2 for v in cnt.values()):
            return ""

        # max-heap by negative counts
        heap = [(-v, ch) for ch, v in cnt.items()]
        heapq.heapify(heap)

        res = []
        while len(heap) >= 2:
            v1, c1 = heapq.heappop(heap)
            v2, c2 = heapq.heappop(heap)
            res.append(c1)
            res.append(c2)
            if v1 + 1 < 0:  # v1 is negative
                heapq.heappush(heap, (v1 + 1, c1))
            if v2 + 1 < 0:
                heapq.heappush(heap, (v2 + 1, c2))

        if heap:
            res.append(heap[0][1])  # last remaining char (count must be 1)
        return "".join(res)
