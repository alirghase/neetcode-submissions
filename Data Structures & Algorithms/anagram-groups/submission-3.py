class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_list = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams_list:
                anagrams_list[sorted_word].append(word)
            else:
                anagrams_list[sorted_word] = [word]
        
        return list(anagrams_list.values())
