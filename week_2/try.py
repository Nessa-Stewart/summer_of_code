filename = "alice_in_wonderland.txt"
file = open(filename, "r")

alphabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
letter =[]
letterfreq = []

raw = file.read()

def count_letters(text):
	text=text.lower()
	for char in alphabet:
		count=0
		for c in text:
			if c == char:
				count+=1
		letter.append(char)
		letterfreq.append(str(count))

count_letters(raw)

alphacount=list(zip(letter, letterfreq))

print(alphacount)

# filename = "alice_in_wonderland.txt"
# file = open(filename, "r")

# from string import ascii_lowercase

# def count_letters(text):
# 	text=text.lower()
# 	for char in ascii_lowercase:
# 		count=0
# 		for c in text:
# 			if c == char:
# 				count+=1
# 		print("Number of letter " + char + ": " + str(count))

# raw = file.read()

# count_letters(raw)