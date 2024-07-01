# Checking if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = "racecar"
print(is_palindrome(s))
# Output: True