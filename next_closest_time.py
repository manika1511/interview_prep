from itertools import permutations


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        minutes = int(time[:2]) * 60 + int(time[3:])
        digits = set([int(x) for x in time if x != ":"])

        while True:
            minutes = (minutes + 1) % (24 * 60)
            digit_list = [minutes / 60 / 10, minutes / 60 % 10, minutes % 60 / 10, minutes % 60 % 10]
            is_valid = True
            for digit in digit_list:
                if digit not in digits:
                    is_valid = False

            if is_valid == True:
                return "{:02d}:{:02d}".format(minutes / 60, minutes % 60)
