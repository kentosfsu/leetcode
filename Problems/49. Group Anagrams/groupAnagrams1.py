# O(NKlogK) N: len(strs), K: max(len(s))
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) #{aet: [eat, tea]}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            group[s_sorted].append(s)
        return group.values()