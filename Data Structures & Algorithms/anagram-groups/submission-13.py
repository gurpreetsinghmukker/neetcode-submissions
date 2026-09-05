from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            char_list = tuple(sorted(s))
            str_dict[char_list].append(s)
        return list(str_dict.values())
