class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        ascending_index = sorted(range(n), key=lambda i: A[i])
        odd_next_hop = self.find_next_hop(ascending_index)
        descending_index = sorted(range(n), key=lambda i: -A[i])
        even_next_hop = self.find_next_hop(descending_index)

        odd = [False]*n
        even = [False]*n

        odd[-1] = True
        even[-1] = True

        for i in reversed(range(n-1)):
            odd_next, even_next = odd_next_hop[i], even_next_hop[i]
            if odd_next:
                odd[i] = even[odd_next]
            if even_next:
                even[i] = odd[even_next]

        return sum(odd)


    def find_next_hop(self, index_list):
        next_hop = [None]*len(index_list)
        stack = []

        for i in index_list:
            while stack and stack[-1] < i:
                next_hop[stack.pop()] = i
            stack.append(i)
        return next_hop