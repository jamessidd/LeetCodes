class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currstring = ""
        currnum = 0

        for char in s:

            if char.isdigit():
                currnum = currnum * 10 + int(char)

            elif char == "[":
                stack.append((currstring, currnum))
                #reset
                currstring = ""
                currnum = 0
            elif char == "]":

                prevstr, num = stack.pop()
                currstring = prevstr + currstring * num
            else:
                currstring += char

        return currstring