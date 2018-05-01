'''
Problem Number: 350
Difficulty level: Easy
Link: https://leetcode.com/problems/
Author: namratabilurkar
'''

'''
Input:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2]

Output:
[2, 2]
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection_list = []

        if len(nums1) > len(nums2):
            self.intersection_finder(nums1, nums2, intersection_list)
        else:
            self.intersection_finder(nums2, nums1, intersection_list)

        return intersection_list

    def intersection_finder(self, l1, l2, output_list):
        """
        Finds the intersection
        :param l1: longer list List[int]
        :param l2: smaller list List[int]
        :param output_list: Intersection list List[int]
        :return: List[int]
        """
        for i in l2:
            if i in l1:
                output_list.append(i)
                l1.remove(i)

        return output_list

output = Solution()
print(output.intersect(nums1 = [1, 2, 2, 1], nums2 = [2, 2])) # [2, 2]
print(output.intersect(nums1 = [3,1,2], nums2 = [1, 1])) # [1]