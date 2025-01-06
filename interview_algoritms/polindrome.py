# Checking if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = "racecar"
print(is_palindrome(s))
# Output: True


def is_palindrome(s):
    # Initialize two pointers
    left = 0
    right = len(s) - 1

    # Iterate until the pointers cross
    while left < right:
        # Compare characters
        if s[left] != s[right]:
            return False
        # Move the pointers towards the center
        left += 1
        right -= 1

    # If all characters match, it's a palindrome
    return True

# Examples
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

# Satih qa manager
