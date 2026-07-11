
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
            
            
            for i in strs[:]:

                valid = True
                
                for j in i:
                    if valid: 
                        if j in listOfLetters:
                            listOfLetters.remove(j)
                        else:
                            valid = False

                if valid:
                    print(i)
                    sameAnagrams.append(i)
                    strs.remove(i)
                 
            groupedAnagram.append(sameAnagrams)

        return groupedAnagram


sol = Solution()
words = ["eat","tea","tan","ate","nat","bat"]

print(f"The result is {sol.groupAnagrams(words)}")