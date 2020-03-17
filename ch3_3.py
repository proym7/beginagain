word = input ("Enter a word to search for vowels: ")

vowel = set('aeiou')

found = vowel.intersection(set(word))

for vowel in found:
    print(vowel)
