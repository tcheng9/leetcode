'''
0. Question notes:
-----------------------------------------------
'''

#Optimizing old solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
       


        dictionary = defaultdict(list)
        for i in range(len(strs)):

            array = [0] * 26

            for letter in strs[i]:
                array[ord(letter) - ord('a')] += 1
            dictionary[array].append(strs[i])
            

        return dictionary.values()


###Issue: You can't use an array as a dictonary key so you must use a tuple as the key. 
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
       


        dictionary = defaultdict(list)
        for i in range(len(strs)):

            array = [0] * 26

            for letter in strs[i]:
                array[ord(letter) - ord('a')] += 1
            dictionary[tuple(array)].append(strs[i])
            

        return dictionary.values()

'''
I. Conceptual Solution
-----------------------------------------------
'''




'''
II. Implementation
-----------------------------------------------
'''




'''
III. Code solutions
-----------------------------------------------
'''

##Altnerative solution
'''
This solution sorts the words into an array and uses those unique sorted words as the way to check for anagrams. 
ie tea and eat are anagrams -> when sorted alphabetically, they are both "aet"

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
                
            sorted_word_as_array = sorted(word)
            word_as_string = ''.join(sorted_word_as_array)

            res[word_as_string].append(word)


        
            

        return res.values()

'''
IV. Summary
-----------------------------------------------
Takeaways:
1. Learn how to build a dictionary via an array
2. Remember ord(letter) - ord('a') -> any letter is always >= ord('a') (or ord('A'), if you are working with capital letters)
3. Dictionarys cannot have arrays as keys because they are not hashable. You need to convert the array into a tuple
4. Learned the "sorted(put_variable_or_word_here)" -> (1) it takes a string, (2) changes the string into a sorted array 
5. Learned the join function -> Given an already existing string, it takes an array and combines the values in the array by some (optional) delimiter
    Note: whatever you put into the '' before the .join() will be the delimiter
    a. example: ''.join(array) -> 'abc'
    b. example: '#'.join(array) -> 'a#b#c'
'''


