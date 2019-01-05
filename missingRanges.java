/*
 *
 * Problem Number: 163
 * Difficulty level: Medium
 * Link: https://leetcode.com/problems/missing-ranges/
 * Author: namratabilurkar
 */

/*
Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

 */
class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        /*
        Check the difference between the previous number and the next number:
        If it is --
            1. 0, then do nothing.
            2. 1, then add the number of nums[i] + 1 to the outputArr
            3. >1, then find the lower range and the upper range, add
                "lowerRange->upperRange" to the outputArr
        */
        List<String> outputArr = new ArrayList<String>();

        int n = nums.length;

        if ((nums.length == 0) || nums == null) {
            outputArr.add(rangeOutput(lower, upper));
            return outputArr;
        }
        int prev = lower;

        for (int i=0; i<nums.length; i++) {
            if (prev < nums[i]) {
                outputArr.add(rangeOutput(prev, nums[i]-1));
            }

            if (nums[i] < upper) {
                prev = nums[i]+1;
            } else {
                break;
            }
        }
        if (nums[n-1] < upper) {
            outputArr.add(rangeOutput(nums[n-1]+1, upper));
        }
        return outputArr;
    }

    private String rangeOutput(int low, int high) {

        if (high-low == 0) {
            return String.valueOf(low);
        }
        return low + "->" + high;
    }
}