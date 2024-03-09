def count_character_occurrences(input_string, character):
    return input_string.count(character)

# Test the function
print(count_character_occurrences("hello world!", 'l'))  # Should return 3
print(count_character_occurrences("hello world!", 'h'))  # Should return 0
