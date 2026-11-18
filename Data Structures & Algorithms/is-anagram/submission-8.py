class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one dict
        anagram_dict = {}
        for char in s:
            if char in anagram_dict:
                anagram_dict[char] += 1
            else:
                anagram_dict[char] = 1
        # {'a': 1}
        for char in t:
            if char in anagram_dict:
                anagram_dict[char] -= 1
            else:
                anagram_dict[char] = -1
        
        # {'a': 0, 'c' = -2}
        for i in anagram_dict.values():
            if i != 0:
                return False
        return True