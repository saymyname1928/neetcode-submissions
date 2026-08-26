from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word))
            anagrams[word_sorted].append(word)
            
        return list(anagrams.values())
            

        