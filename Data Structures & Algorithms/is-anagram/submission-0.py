class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1_dict = {}
        word2_dict = {}
        if len(s)!=len(t):
            return False
        
        for i in s:
            if word1_dict.get(i, None):
                word1_dict[i] = word1_dict[i] + 1
            else:
                word1_dict[i] = 1
        
        for i in t:
            if word2_dict.get(i, None):
                word2_dict[i] +=1
            else:
                word2_dict[i] = 1
        
        if len(word1_dict.keys())!= len(word2_dict.keys()):
            return False
        
        for key, val in word1_dict.items():
            if not key in word2_dict:
                return False
            if not val == word2_dict[key]:
                return False
        return True