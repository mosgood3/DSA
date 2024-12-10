from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitstoChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtrack(i,curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitstoChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        return res
if __name__ == '__main__':
    solution = Solution()
    testDigits = "45"
    result = solution.letterCombinations(testDigits)
    print(f"Input digits: {testDigits}")
    print("Output combinations:", result)


#Time and space complexity = O(4^n)
#Time and Space Complexity
###The given Python code generates all possible letter combinations that each number on a phone map to, based on a string of digits. Here is an analysis of its time and space complexity:
###    Time Complexity: Let n be the length of the input string digits. The algorithm iterates through each digit, and for each digit, iterates through all the accumulated combinations so far to add the new letters.
###    For a digit i, we can have at most 4 letters (e.g., for digits mapping to 'pqrs', 'wxyz') which increases the number of combinations by a factor of up to 4 each time. Thus, in the worst case scenario, the time complexity can be expressed as O(4^n), as each step could potentially multiply the number of combinations by 4.
###    Space Complexity: The space complexity is also O(4^n) because we store all the possible combinations of letters. Although the list ans is being used to keep track of intermediate results, its size grows exponentially with the number of digits in the input. At each step, the new list of combinations is up to 4 times larger than the previous one until all digits are processed.
