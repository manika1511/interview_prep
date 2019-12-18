class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_dict = {}
        for key in range(numCourses):
            adj_dict[key] = []
        for item in prerequisites:
            adj_dict[item[1]].append(item[0])

        global is_possible
        is_possible = True

        def top_sort(adj_dict, current, visited, stack):
            global is_possible
            if not is_possible:
                return
            visited[current] = "slight"
            for j in adj_dict[current]:
                if visited[j] == "False":
                    top_sort(adj_dict, j, visited, stack)
                elif visited[j] == "slight":
                    is_possible = False
            visited[current] = "True"
            stack.insert(0, current)

        visited = ["False"] * numCourses
        stack = []
        for i in range(numCourses):
            if visited[i] == "False":
                top_sort(adj_dict, i, visited, stack)
        if is_possible == True:
            return stack
        else:
            return []