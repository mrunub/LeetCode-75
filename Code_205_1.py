# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = dict()
        for i, j in zip(s, t):
            if i not in mappings.keys() and j not in mappings.values():
                mappings[i] = j
            elif i in mappings.keys() and j in mappings.values() and mappings[i] == j:
                pass
            else:
                return False
        return True


s = Solution()
print(s.isIsomorphic("bbbaaaba", "aaabbbba"))

# Test Cases
#
# add egg
# foo bar
# paper title
# badc baba
# bbbaaaba aaabbbba
