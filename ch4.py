def search4vowels():
    vowels = set('aeiou')
    word = input ("enter a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
    
search4vowels()
