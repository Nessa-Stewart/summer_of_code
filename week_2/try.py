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

