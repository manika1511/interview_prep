import math
from operator import itemgetter


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # dist_list = []
        # for point in points:
        #     dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
        #     dist_list.append(dist)
        #
        # d = [list(x) for x in zip(*sorted(zip(dist_list, points), key=itemgetter(0)))]
        # dist_sorted, points_sorted = d[0], d[1]
        points_sorted = sorted(points, key=lambda point: sqrt(point[0] ** 2 + point[1] ** 2))

        return points_sorted[0:K]
