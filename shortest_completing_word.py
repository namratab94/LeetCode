'''
Problem Number: 748
Difficulty level: Easy
Link: https://leetcode.com/problems/shortest-completing-word/
Author: namratabilurkar
'''

'''
Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.


Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.
'''

import collections as c


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lp_map = dict()

        for i in range(len(licensePlate)):
            if licensePlate[i].isalpha():
                if licensePlate[i] not in lp_map:
                    lp_map[licensePlate[i].lower()] = 0
                    lp_map[licensePlate[i].lower()] += 1
                else:
                    lp_map[licensePlate[i].lower()] += 1

        char_sum = 0

        for i in lp_map:
            if i.isalpha():
                char_sum += lp_map[i]

        # words.sort(key=len)

        more_than_char_sum = list(filter(lambda x: len(x) >= char_sum, words))

        print(lp_map)
        print(char_sum)
        print(words)
        print(more_than_char_sum)


        short_word = ''
        for word in more_than_char_sum:
            word_map = c.Counter(word.lower())
            print(word_map)
            for each_char in lp_map:
                if each_char in word_map and word_map[each_char] >= lp_map[each_char]:
                    continue
                else:
                    break
            short_word = word
            if short_word != '' and len(word) < len(short_word):
                short_word = word
        return short_word


obj = Solution()
# output = obj.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"])
output = obj.shortestCompletingWord(licensePlate = "Ah71752", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"])
print(output)