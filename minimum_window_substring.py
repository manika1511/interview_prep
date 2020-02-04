from collections import Counter
class Solution(object):
        def minWindow(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: str
            """

            if not t or not s:
                return ""
            dict_t = Counter(t)

            required = len(dict_t)

            l, r = 0, 0

            formed = 0
            window_counts = {}
            ans = (float("inf"), l, r)

            while r < len(s):
                character = s[r]
                window_counts[character] = window_counts.get(character, 0) + 1
                if character in dict_t and window_counts[character] == dict_t[character]:
                    formed += 1

                while l <= r and formed == required:
                    character = s[l]
                    if r - l + 1 < ans[0]:
                        ans = (r - l + 1, l, r)
                    window_counts[character] -= 1
                    if character in dict_t and window_counts[character] < dict_t[character]:
                        formed -= 1
                    l += 1

                # Keep expanding the window once we are done contracting.
                r += 1
            return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]

