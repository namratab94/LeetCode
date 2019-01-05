/*
 *
 * Problem Number: 371
 * Difficulty level: Easy
 * Link: https://leetcode.com/problems/sum-of-two-integers/
 * Author: namratabilurkar
 */

/*

Exmaple 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = -2, b = 3
Output: 1
 */

class Solution {
    public int getSum(int a, int b) {
        // Approach 1:
        while (b!=0) {

            int carry = a & b;

            a = a ^ b;

            b = carry << 1;

        }
        return a;

        // Approach 2:
        /*
        // a^2 - b^2 = (a+b) * (a-b)
        => (a+b) = (a*a - b*b)/(a-b)
        */
        // return (((a*a) - (b*b))/(a-b));
    }
}