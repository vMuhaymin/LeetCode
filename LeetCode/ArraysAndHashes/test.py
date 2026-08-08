class Solution:
    def groupAnagrams(self, strs):
        res = {}

        for word in strs:
            sortedLetters = "".join(sorted(word))
            if sortedLetters not in res:
                res[sortedLetters] = [word]
            else:
                res.get(sortedLetters).append(word)

        return list(res.values())