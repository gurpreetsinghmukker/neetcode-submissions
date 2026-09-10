class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = []
        for char in s:
            if (char>='A' and char<='z') or (char>="0" and char<="9"):
                char_list.append(char.lower())
        for i, c in enumerate(char_list):
            if not char_list[i] == char_list[len(char_list)-1-i]:
                return False
        return True
        