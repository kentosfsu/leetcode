# O(NK) N: len(strs), K: max(len(s))
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) #{tuple(1(a),0,0,0,1(e),0,..): [eat, tea]}
        for s in strs:
            alph_count = [0 for _ in range(26)]
            for c in s:
                alph_count[ord(c)-ord('a')] += 1
            group[tuple(alph_count)].append(s)
        return group.values()