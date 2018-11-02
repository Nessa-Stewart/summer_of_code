filename = "alice_in_wonderland.txt"
file = open(filename, "r")

from string import ascii_lowercase

def count_letters(text):
	text=text.lower()
	for char in ascii_lowercase:
		count=0
		for c in text:
			if c == char:
				count+=1
		print("Number of letter " + char + ": " + str(count))

raw = file.read()

count_letters(raw)