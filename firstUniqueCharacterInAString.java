/*
*
* Problem Number: 387
* Difficulty level: Easy
* Link: https://leetcode.com/problems/first-unique-character-in-a-string/
* Author: namratabilurkar
*/

/*
Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

 */
class Solution {
    public int firstUniqChar(String s) {
        int firstNonRepeatingCharIndex = -1;

        for (int i=0; i<s.length(); i++) {
            char currChar = s.charAt(i);
            if (s.indexOf(currChar) == s.lastIndexOf(currChar)) {
                firstNonRepeatingCharIndex = i;
                return firstNonRepeatingCharIndex;
            }
        }
        return firstNonRepeatingCharIndex;
    }
}