from itertools import permutations


input_string = input('Word: ')
foundWord = False

# taken from https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
perms = perms = [''.join(p) for p in permutations(input_string.lower())]
# print(perms)

with open('dictionary_words.txt', 'r') as f:
    for line in f:
      word = line.rstrip('\n')
      if word in perms:
          print(word)
          foundWord = True

if foundWord == False:
    print('No matches found')

