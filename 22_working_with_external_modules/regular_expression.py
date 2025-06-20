import re 
text = "The rain in Spain"
# Find all occurrences of 'ain' in the text ]
matches = re.findall(r'ain', text)
print(matches)  # Output: ['ain', 'ain']

matches = re.findall(r'\bain\b', text)
print(matches)  # Output: ['ain'] (matches 'ain' as a whole word)   


# Find all occurrences of 'ain' at the end of a word
matches = re.findall(r'ain\b', text)    
print(matches)  # Output: ['ain'] (matches 'ain' at the end of a word)


re.sub(r'ain', 'XYZ', text)  # Replace 'ain' with 'XYZ'
print(re.sub(r'ain', 'XYZ', text))  # Output: The rXYZ in SpXYZ

re.escape(r'The rain in Spain')  # Escape special characters in the string
print(re.escape(r'The rain in Spain'))  # Output: Thez\ rain\ in\ Spain (escapes spaces and other special characters)