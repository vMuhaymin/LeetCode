
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

                valid = True
                newList = []
                for letter in listOfLetters:
                    newList.append(letter)
                    
                
                for j in otherWord:
                    if valid: 
                        if j in newList:
                            if len(j) == len(word):
                                newList.remove(j)
                                print(j)
                            else:
                                valid= False
                        else:
                            valid = False

                if valid:
                    sameAnagrams.append(otherWord)
                    strs.remove(otherWord)
                 
            groupedAnagram.append(sameAnagrams)

        return groupedAnagram


sol = Solution()
words =["ac","c"]

print(f"The result is {sol.groupAnagrams(words)}")