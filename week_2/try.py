filename = "alice_in_wonderland.txt"
file = open(filename, "r")



raw = file.read()

raw = raw.lower()

raw = [list(line.rstrip()) for line in raw]

alphabet = ['abcdefghijklmnopqrstuvwxyz']
alphabet = [list(line.rstrip()) for line in alphabet]
letterfreq = []
letter =[]

letter.append(raw)

#print(letter)
#print(alphabet)

hits = [
	(alphabet[i], letter.count(alphabet[i]))
	for i in range(len(alphabet))
	if letter.count(alphabet[i])
]

print(hits)


	



