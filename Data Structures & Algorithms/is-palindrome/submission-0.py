class Solution:
    def isPalindrome(self, s: str) -> bool:

        def clean_string(s: str) -> str:
            cleaned_chars = []

            for char in s:
                if char.isalnum():
                    cleaned_chars.append(char.lower())
            return ''.join(cleaned_chars)

        new_s = clean_string(s)
        s = clean_string(s)
        return s == new_s[::-1]