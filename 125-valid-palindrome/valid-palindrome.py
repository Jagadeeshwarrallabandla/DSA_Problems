class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        convertion = s.lower() # Converted all letters to lower cases
        result = ""

        for ch in convertion:
            if ch.isalnum():
                result += ch

        left = 0
        right = len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False

            left += 1
            right -= 1
        return True

        