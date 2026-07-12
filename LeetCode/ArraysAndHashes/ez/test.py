
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


sol = Solution()
words =["eat","tea","tan","ate","nat","bat"]

print(f"The result is {sol.groupAnagrams(words)}")