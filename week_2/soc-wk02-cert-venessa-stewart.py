#DAY 1

# Calculate a table for each letter in the alphabet from a-z, and count how many times each 
#letter appears in Alcie in Wonderland (fancy word for counting stuff is "frequency distribution" 
#-because you are counting the frquency of something)


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

#DAY 2

#numbers to letters

# for i in range(1,256):
#     print(i, " stands for ", chr(i))

#fix the above so it prints only A-Z and a-z

for i in range(65, 65+2*32):
	if chr(i).isalpha():
		print(i, " stands for ", chr(i))

#Make a function that prints A-Z and a-z

def alphaprint():
	for i in range(65,123):
		if chr(i).isalpha():
			print(chr(i))

alphaprint()

#Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher;))
#I LOVE YOU" [73, , 76,...]

message = input("Give me a message to cypher: ")

cypher = []

def cyphermaker(text):
	for c in text:
		cypher.append(ord(c))

cyphermaker(message)

print(cypher)

#Write a function that prints out all elements of the above board, sarting from the first element of the first line, till the end.
# Each line should be read from beginning to end.

M = 'land'
o = 'water'
world = [
         [o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [o,o,o,M,M,M,M,M,M,M,o],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]
        ]

def forwards():
	for i in world:
		print(*i)

forwards()

#Now write a function that prints out all elements in reverse.


