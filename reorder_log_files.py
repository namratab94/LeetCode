'''
Problem Number: 937
Difficulty level: Easy
Link: https://leetcode.com/problems/reorder-log-files/
Author: namratabilurkar
'''

'''
Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # Objective is to define a custom sorter.
        '''
        GIVEN SOLUTION:

        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
        '''

        digits = []
        letters = []

        # dividing the logs into two parts, one for digits and another for letters
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: x.split()[0])  # Sort based on the identifier when there is a clash in the letters
        letters.sort(key=lambda x: x.split()[1:])

        result = letters + digits

        return result