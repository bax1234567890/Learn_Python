
def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b >= 0 else -result

# Example usage
print(multiply(3, 2))  # Output: 6
print(multiply(-3, 2))  # Output: -6
print(multiply(3, -2))  # Output: -6
print(multiply(-3, -2))  # Output: 6


def input_string(input, character):
    return input.count(character)

print(input_string('Hello World', 'l'))
print(input_string('Buy World', 'B'))

def input_string(inp, char):
    return inp.count(char)
print(input_string('What is your name jhjhjhjhjhjhjh?', 'j'))


def test_multiply(x, y):
    result = 0
    for i in range(0, y+1):
        result = result +x
        y=y+1
    return result
print(test_multiply(7, 8))


def find_missing(nums):
    # Calculate the length of the input list
    n = len(nums)
    # Calculate the sum of first 'n+1' natural numbers using the formula n*(n+1)/2
    total_sum = n * (n + 1) // 2
    # Calculate the sum of elements in the given list
    array_sum = sum(nums)
    # The missing number is the difference between the total sum and the sum of the array
    return total_sum - array_sum
print(find_missing([1,2,3,4,5,7]))


def multiply(x, y):
    z=0
    for i in range(0, y):
        z=z+x
        # y=y+1
    return z
print(multiply(5, 20))