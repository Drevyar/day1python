def count_vowels_consonants(text):
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    # Convert text to lowercase for case-insensitive counting
    text = text.lower()
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return {
        "vowels": vowel_count,
        "consonants": consonant_count
    }

result = count_vowels_consonants("sa waddee")
print(result)