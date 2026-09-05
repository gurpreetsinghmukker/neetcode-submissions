from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            char_list = tuple(sorted(s))
            # if not str_dict.get(char_list, None) == None:
            str_dict[char_list].append(s)
            # else:
            #     str_dict[char_list] = [s]
        # print(str_dict)
        return list(str_dict.values())
