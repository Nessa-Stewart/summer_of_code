filename = "alice_in_wonderland.txt"
file = open(filename, "r")



raw = file.read()

raw = raw.lower()

#raw = [list(line.rstrip()) for line in raw]

alphabet = ['abcdefghijklmnopqrstuvwxyz']
alphabet = [list(line.rstrip()) for line in alphabet]
letterfreq = []
letter =[]

#letter.append(raw)

#print(letter)
#print(alphabet)



# hits = [
# 	(alphabet[i], letter.count(alphabet[i]))
# 	for i in range(len(alphabet))
# 	if letter.count(alphabet[i])
# ]



# print(hits)

def count_letters(text):
	for char in alphabet:
		count=0
		for c in letter:
			if c == char:
				count+=1
		print(char, str(count))

count_letters(raw)



