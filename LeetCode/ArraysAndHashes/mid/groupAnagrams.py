class Solution:
    def groupAnagrams(self, strs):

        groupedAnagram = {}
        
        for word in strs:
            sortedLetters = "".join(sorted(word))

            if sortedLetters not in groupedAnagram:
                groupedAnagram[sortedLetters] = [word]
            else:
                groupedAnagram.get(sortedLetters).append(word)

        return list(groupedAnagram.values())