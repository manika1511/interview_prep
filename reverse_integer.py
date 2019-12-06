class Solution:
    def reverse(self, x):
        reverse = 0
        flag = 0
        if x < 0:
            flag = 1
        m = len(str(abs(x)))
        n = abs(x)

        while n > 0:
            rem = int(n % 10)
            n = int(n / 10)
            reverse = reverse + rem * (10 ** (m - 1))
            m = m - 1

        if flag == 1:
            reverse = int('-' + str(reverse))
        if reverse < (-2 ** 31) or reverse > (2 ** 31 - 1):
            return 0
        return reverse