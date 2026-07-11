
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        groupedAnagram = []
        while strs:
            sameAnagrams = []

            word = strs.pop(0)
            sameAnagrams.append(word)

            listOfLetters = []

            for i in word:
                listOfLetters.append(i)
            
            
            for otherWord in strs[:]:

                if len(otherWord) != len(word):
                    valid = False
                else:
                    valid = True
                if valid:
                    newList = []
                    for letter in listOfLetters:
                        newList.append(letter)
                        
                    
                    for j in otherWord:
                        if valid: 
                            if j in newList:               
                                newList.remove(j)
                            else:
                                valid = False

                    if valid:
                        sameAnagrams.append(otherWord)
                        strs.remove(otherWord)
                 
            groupedAnagram.append(sameAnagrams)

        return groupedAnagram


sol = Solution()
words =["eat","tea","tan","ate","nat","bat"]

print(f"The result is {sol.groupAnagrams(words)}")