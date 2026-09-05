class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            char_list = sorted([c for c in s])
            if not str_dict.get((*char_list, len(s)), None) == None:
                str_dict[(*char_list, len(s))].append(s)
            else:
                str_dict[(*char_list, len(s))] = [s]
        # print(str_dict)
        return [val for val in str_dict.values()]
