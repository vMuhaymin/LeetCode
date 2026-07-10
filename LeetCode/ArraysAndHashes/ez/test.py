class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupedAnagrams = []
        
        if len(strs) == 1:
            groupedAnagrams.append(strs)
            return groupedAnagrams

        while len(strs) >= 1 :
            anagrams = []
            
            seen = {}
            word = strs.pop()
            anagrams.append(word)

            for j in word:
                if j in seen:
                    seen[j] = seen.get(j) +1 
                else:
                    seen[j] = 1

            for otherWord in strs[:]:
                anotherSeen = {}
                for i in otherWord:
                    if i in anotherSeen:
                        anotherSeen[i] = anotherSeen.get(i) +1
                    else:
                        anotherSeen[i] = 1

                if seen == anotherSeen:
                    anagrams.append(otherWord)
                    strs.remove(otherWord)

            groupedAnagrams.append(anagrams)
        
        return groupedAnagrams


sol = Solution()
words = ["","",""]
print(f"The solution is {sol.groupAnagrams(words)}")
