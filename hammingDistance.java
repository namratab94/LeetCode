/*
 *
 * Problem Number: 461
 * Difficulty level: Easy
 * Link: https://leetcode.com/problems/hamming-distance/
 * Author: namratabilurkar
 */

/*

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

 */

class Solution {
    public int hammingDistance(int x, int y) {

        /*
        1. XOR given two integers
        2. For as long as the field holding the result of step 1 exists, bitwise
            AND it with 1, while counting the bits that are different.
        3. Right shift the resultant variable to right by 1.
        */

        int xor = x^y;
        int sumOfBits = 0;

        while (xor > 0) {

            sumOfBits += xor & 1;
            xor = xor >> 1;
        }
        return sumOfBits;
    }
}
