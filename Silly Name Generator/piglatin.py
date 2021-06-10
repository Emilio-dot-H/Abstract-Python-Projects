
def main():
	word = input("Type some latin to pig: ")
	brk_word = [_ for _ in word]
	print(brk_word)
	end = len(brk_word)

	vowels = ('e', 'a', 'i', 'o', 'u', 'y')
	flag = True

	"""Scan all vowels"""
	for x in vowels:
		if x == brk_word[0]:
			brk_word.append("way")
			print(brk_word)
			flag = False

	if flag == True:
		print("This is a consonant")
		consonant = brk_word[0]
		brk_word.insert(end, consonant)
		brk_word.append("ay")
		del brk_word[0]
		print(brk_word)

	print(''.join(brk_word))



if __name__ == "__main__":
	main()