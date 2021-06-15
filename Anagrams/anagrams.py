import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

anagram_list = []

# input a SINGLE WORD or SINGLE NAME below to find its anagram
#name = 'Foster'
name = input("Type a name or word: ")
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

# sort name & find anagrams
name_sorted = sorted(name)
for word in word_list:
	word = word.lower()
	if word != name:
		if sorted(word) == name_sorted:
			anagram_list.append(word)

#print out list of anagrams
print()
if len(anagram_list) == 0:
	print("You need a larger dictionairy or a new name!")
else:
	print("Anagrams =", *anagram_list, sep='\n')
