#  take a string and check vowels and its count 
text = "Python 3!"
vowels = 'aieouAIEOU'

# Filters out anything that isn't a letter [A-Z, a-z]
only_vowels = [char for char in text if char in vowels]
letter_count = len(only_vowels)
print(letter_count)
