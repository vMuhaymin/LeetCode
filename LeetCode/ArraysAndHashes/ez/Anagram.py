class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
           return False

        unique_first_word = set(s)
        unique_second_word = set(t)
        
        #Frequency of the first word
        freq_word_one = {}
        for i in unique_first_word:
            counter = 1
            for j in s:
               if i == j:
                freq_word_one[i] = counter
                counter += 1
        
        #Frequency of the 2nd word
        freq_word_two = {}
        for i in unique_second_word:
            counter = 1
            for j in t:
               if i == j:
                freq_word_two[i] = counter
                counter += 1
        if len(freq_word_two) != len(freq_word_two):
           return False
        else:
           for i in freq_word_one:
              if i not in freq_word_two:
                 return False
              else:
                 if freq_word_one[i] !=  freq_word_two[i]:
                    return False

        return True