# Calculate a table for each letter in the alphabet from a-z, and count how many times each 
#letter appears in Alcie in Wonderland (fancy word for counting stuff is "frequency distribution" 
#-because you are counting the frquency of something)


filename = "alice_in_wonderland.txt"
file = open(filename, "r")

alphabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
letter =[]
letterfreq = []

def count_letters(text):
	text=text.lower()
	for char in alphabet:
		count=0
		for c in raw:
			if c == char:
				count+=1
		letter.append(char)
		letterfreq.append(str(count))

raw = file.read()


count_letters(raw)

alphacount=list(zip(letter, letterfreq))


print(alphacount)
	
