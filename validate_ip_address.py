'''
Problem Number: 468
Difficulty level: Medium
Link: https://leetcode.com/problems/validate-ip-address/description/
Author: namratabilurkar
'''

'''
Example 1:

Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".


Example 2:

Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".


Example 3:

Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

'''

import re

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        IPV4 = "IPv4"
        IPV6 = "IPv6"
        NEITHER = "Neither"
        DOT = '.'
        COLON = ':'
        ipv6RegexPattern = r'^[\da-fA-F]{1,4}$'

        if len(IP) == 0 or IP[0] == 0:
            return NEITHER

        if DOT in IP:
            ipAddList = IP.split(".")
            if len(ipAddList) == 4:
                for eachIP in ipAddList:
                    eachIP = str(eachIP)
                    if eachIP.isdigit():
                        if int(eachIP) > 255:
                            return NEITHER
                        if len(eachIP) > 1 and eachIP[0] == "0":
                            return NEITHER
                    else:
                        return NEITHER
            else:
                return NEITHER
            return IPV4

        if COLON in IP:
            ipAddList = IP.split(":")
            if len(ipAddList) == 8:
                for eachIP in ipAddList:
                    if not re.match(ipv6RegexPattern, eachIP):
                        return NEITHER
                return IPV6
            else:
                return NEITHER

        return NEITHER