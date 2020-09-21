vowels = set('aeiou')
word = input('provide a word to search for vowels:')

found = vowels.intersection(set(word))

for k in found:
    print(k)
    
    
      

