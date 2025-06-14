class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_value_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        roman_list = [roman_to_value_dict[char] for char in s]
        result = 0
        skip_a_loop = False
        for i, number in enumerate(roman_list):
            if i == len(roman_list) - 1 and not skip_a_loop:
                result += roman_list[i]
            elif i == len(roman_list) - 1 and skip_a_loop:
                break
            elif skip_a_loop:
                skip_a_loop = False
                continue
            elif number >= roman_list[i+1]:
                result += roman_list[i]
            elif number < roman_list[i+1]:
                result += roman_list[i+1] - roman_list[i]
                skip_a_loop = True
            else:
                raise ValueError("Invalid Roman numeral")
        return result


if __name__ == "__main__":
    s = "III"
    solution = Solution()
    print(solution.romanToInt(s))

    s = "LVIII"
    solution = Solution()
    print(solution.romanToInt(s))

    s = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(s))
