class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """

        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        current_max = 0
        max_val = 0

        for fruit in tree:
            if fruit == last_fruit or fruit == second_last_fruit:
                current_max = current_max + 1
            else:
                current_max = last_fruit_count + 1

            if fruit == last_fruit:
                last_fruit_count = last_fruit_count + 1
            else:
                second_last_fruit = last_fruit
                last_fruit = fruit
                last_fruit_count = 1

            max_val = max(max_val, current_max)

        return max_val
