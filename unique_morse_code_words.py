'''
Problem Number: 804
Difficulty level: Easy
Link: https://leetcode.com/problems/unique-morse-code-words/description/
Author: namratabilurkar
'''
'''
Alphabets in morse code:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

'''

'''
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''

from string import ascii_lowercase


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        '''
        Read the list of morse code
        Create a dict mapping alphabets with their morse code
        Create a new set that holds morse code equivalent of given list "words"
        Return the length of the set
        '''
        morse_code_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                           "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabets = [ascii_lowercase[i] for i in range(26)]
        alphabet_morse_code_map = dict()
        morse_set = set()

        for i in range(26):
            alphabet_morse_code_map[alphabets[i]] = morse_code_list[i]

        for word in words:
            temp_word = ""
            for char in word:
                morse_char = alphabet_morse_code_map[char]
                temp_word += morse_char
            morse_set.add(temp_word)

        return len(morse_set)
