class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            char_list = ''.join(sorted(s))
            if not str_dict.get(char_list, None) == None:
                str_dict[char_list].append(s)
            else:
                str_dict[char_list] = [s]
        # print(str_dict)
        return [val for val in str_dict.values()]
