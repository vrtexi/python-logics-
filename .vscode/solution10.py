# Take a string and count how many vowels it contains.

# Example:
# "hello world" → 3

text = "Python 3!"
vowels = 'aieouAIEOU'

# Filters out anything that isn't a letter [A-Z, a-z]
only_vowels = [char for char in text if char in vowels]
letter_count = len(only_vowels)
print(letter_count)

# print the vowels that are in the word
# using set intersection
set_word = "hellow world"
set_vowel = set("aeiou")

unique_vowel = set(set_word.lower()).intersection(set_vowel)
print(unique_vowel)