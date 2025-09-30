"""

Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""

#text = input('Enter text :')


text = 'The Quick Brown Fox Jumps Over The Lazy Dog'

total_withs_space = len(text)
total_with_out_space = len(text.replace(' ', ''))

# Character Analysis
vowels = 'aeiouAEIOU'
vowels_count = sum(text.count(i) for i in vowels)
consonant_count = total_with_out_space - vowels_count
char_freq = {}
for char in text.lower():
    if char.isalpha():
        char_freq[char] = char_freq.get(char, 0) + 1
most_frequent_char = max(char_freq.items(), key=lambda x: x[1], default=(' ', 0))[0]
most_frequent_count = char_freq.get(most_frequent_char, 0)


# Word Analysis
words = text.split()
total_words = len(words)



print("\n=== TEXT ANALYSIS REPORT ===")
print("Character Analysis:")
print(f"- Total characters: {total_withs_space} (with spaces), {total_with_out_space} (without spaces)")
print(f"- Vowels: {vowels_count}")
print(f"- Consonants: {consonant_count}")
print(f"- Most frequent: '{most_frequent_char}' (appears {most_frequent_count} times)")


print("\nWord Analysis:")
print(f"- Total words: {total_words}")