'''
Problem Number: 929
Difficulty level: Easy
Link: https://leetcode.com/problems/unique-email-addresses/
Author: namratabilurkar
'''


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        '''
        Rules:
        1. Convert everything to lowercase.
        2. Split on '@', the left part is the local name and the right half is the domain name.
        3. Strip '.' from the local part of the name
        4. Strip everything in local part including and after '+'
        '''

        unique_email_set = set()

        for each_email in emails:
            final_email = ""

            # Converting all the characters in the email to lowercase
            each_email = each_email.lower()

            # Obtaining the local part of the email and removing all the periods
            local_name = each_email.split('@')[0].replace('.', '')

            # Obtaining the domain part of the email
            domain_name = each_email.split('@')[1]

            # Removal of '+' from the local part of the email
            at_index = local_name.index('+')  # Obtained the index of the first occurrence of the '+' character
            local_name = local_name[
                         :at_index]  # Retain everything in the local part from the beginning to the first occurrence of '+'

            # Rebuilding the final email after cleaning
            final_email += local_name + "@" + domain_name

            # Adding the final email to the set containing all the valid email addresses
            unique_email_set.add(final_email)

        return len(unique_email_set)