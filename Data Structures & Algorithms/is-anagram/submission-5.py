class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap of s
        # hashmap of t

        anagram_s, anagram_t = {}, {}
        for char in s:
            if char in anagram_s:
                anagram_s[char] += 1
            else:
                anagram_s[char] = 1
        for char in t:
            if char in anagram_t:
                anagram_t[char] += 1
            else:
                anagram_t[char] = 1
        
        return anagram_s == anagram_t