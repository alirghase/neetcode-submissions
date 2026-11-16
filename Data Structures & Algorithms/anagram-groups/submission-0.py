class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = {}

        for word in strs: 
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams_group:
                anagrams_group[sorted_word].append(word)
            else:
                anagrams_group[sorted_word] = [word]
        
        return list(anagrams_group.values())
    