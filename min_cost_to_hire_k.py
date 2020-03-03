from heapq import heappush, heappop


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n = len(quality)
        workers = []
        for i in range(n):
            workers.append((float(wage[i]) / quality[i], quality[i]))

        workers = sorted(workers, key=lambda x: x[0])
        sum_q = 0
        ans = 0
        k_min_quality = []
        for i in range(K):
            sum_q = sum_q + workers[i][1]
            heappush(k_min_quality, workers[i][1] * (-1))

        ans = sum_q * workers[K - 1][0]

        for i in range(K, n):
            max_q = abs(k_min_quality[0])
            if max_q > workers[i][1]:
                heappop(k_min_quality)
                heappush(k_min_quality, workers[i][1] * (-1))
                sum_q = sum_q + workers[i][1] - max_q

            ans = min(ans, sum_q * workers[i][0])
        return ans