class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram: dict = {}

        for i, word in enumerate(strs):
            key: str = "".join(sorted(word))

            if key not in anagram:
                anagram[key] = []
            anagram[key].append(word)

        result:List[List[str]] = list(anagram.values())
        return result
