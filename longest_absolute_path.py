'''
Problem Number: 388
Difficulty level: Medium
Link: https://leetcode.com/problems/longest-absolute-file-path/description/
Author: namratabilurkar
'''
'''
Input: "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20

Input: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
'''

from collections import OrderedDict
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        pathDict = OrderedDict()
        TAB = '\t'
        DOT = '.'
        '''
        -- Split the input string on '\n' to obtain inputList.
        -- Iterate through each entry in the inputList and create common 
            paths based on the count of new tabs.
        -- Keep track of the count of '\t' and map it to the paths 
        -- Eg: pathDict = {
        0  : {
                0 : (3, False)
        },
        1 : {
                0 : (11, False),
                1 : (11, False)   
        },
        2 : {
                0 : (20, True)
            }
        }
        -- Iterate through pathDict, determine and return the lengthOfLongestAbsolutePath.
        
        '''
        inputList = input.split('\n')
        for i in inputList:
            flag = False
            tabCount = i.count(TAB)
            currVal = i.strip(TAB)
            iLen = len(currVal)
            if tabCount not in pathDict:
                pathDict[tabCount] = OrderedDict()
                counter = 0
            if tabCount == 0:
                if DOT in currVal:
                    flag = True
                pathDict[tabCount][counter] = (iLen, flag)
            else:    
                path = pathDict[tabCount-1][pathDict[tabCount-1].keys()[-1]]
                val = path[0]
                if DOT in currVal:
                    flag = True
                pathDict[tabCount][counter] = ((val + 1 + iLen), flag)
                counter += 1
        
        lengthOfLongestAbsolutePath = 0
        for path in pathDict:
            for subPath in pathDict[path]:
                tempPathLength = pathDict[path][subPath][0]
                flag = pathDict[path][subPath][1]
                if flag and tempPathLength > lengthOfLongestAbsolutePath:
                    lengthOfLongestAbsolutePath = tempPathLength
        return lengthOfLongestAbsolutePath