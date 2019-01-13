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

M = 'M'
o = '-'
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

M = 'M'
o = '-'
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

def reverse(world):
	world = [listElem[::-1] for listElem in world[::-1]]
	return world

world = reverse(world)

print('\n'.join(' '.join(str(cell) for cell in row) for row in world))

#There is one small bug in the continent counter above. Can you find it and fix it? (Hint:change the 
#world so that the continent borders the edge)

M = 'M'
o = '-'
world = [
		 [o,o,o,o,o,o,o,o,o,o,o],
		 [o,o,o,o,M,M,o,o,o,o,o],
		 [o,o,o,o,o,o,o,o,M,M,o],
		 [o,o,o,M,o,o,o,o,o,M,o],
		 [o,o,o,M,o,M,M,o,o,o,o],
		 [o,o,o,o,M,M,M,M,o,o,o],
		 [o,o,o,M,M,M,M,M,M,M,M],
		 [o,o,o,M,M,o,M,M,M,o,o],
		 [o,o,o,o,o,o,M,M,o,o,o],
		 [o,M,o,o,o,M,o,o,o,o,o],
		 [o,o,o,o,o,o,o,o,o,o,o]
		]



def continent_counter(world, x, y):
	if(x>10 or x<0) or (y>10 or y<0):
		return 0
	if world[y][x] != 'M':
	# Either it's water or we already counter it,
	# but wither way, we don't want to count it now.
		return 0

	#So firest we count this tile....
	size = 1
	world[y][x] = 'counted land'
	#...then we count all of the neighboring eight tiles
	#(and, of course, their neighbors by way of the recursion).

	size = size + continent_counter(world, x-1,y-1)
	size = size + continent_counter(world, x, y-1)
	size = size + continent_counter(world, x+1, y-1)
	size = size + continent_counter(world, x-1, y )
	size = size + continent_counter(world, x+1, y )
	size = size + continent_counter(world, x-1, y+1)
	size = size + continent_counter(world, x , y+1)
	size = size + continent_counter(world, x+1, y+1)
	return size

print(continent_counter(world, 5,5))

#Write a function that geneerates a n xn sized board with either land or water chosen randomly

import random

tile = ['-', 'M']

board = []

def generate(n):
	return[board.append(random.choice(tile))for i in range(n) for j in range(n)]

number = int(input("Give me a number for square board size: "))

generate(number)

board = [board[x:x+(number)]for x in range(0, len(board), (number))]

print('\n'.join(' '.join(str(cell) for cell in row) for row in board))

#Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone 
#who shared their dream.

class Student():
	def __init__(self, name, discord_id, fav_food, dream):
		self.name = name
		self.discord_id = discord_id
		self.fav_food = fav_food
		self.dream = dream

	def my_print(self):
		print(self.name + ", " + self.discord_id + ", " + self.fav_food + ", " + self.dream)


s1 = Student("Virginia Balsiro", "yesviginia [Gold] [Volunteer]", "pasta", "Moving to Europe")
s2 = Student("Andrea Visanoiu", "Andrea[Gold]", "wontonmee", "teaching university")
s3 = Student("Cristina Tarantino", "CristyTarantino[Gold]", "pasta", " Being an amazing developer")
s4 = Student("Deb Cupitt", "DebCupitt[Gold]", "chocolate", "Gender equality")
s5 = Student("Marwa Qabell", "Marwa Qabeel[Gold]", "chocolate", "Data Analyst")
s6 = Student("Sacha Young", "Sacha[Gold]", "french fries", "To return to research")
s7 = Student("Jessica", "Jessi_RS[Gold]", "pasta", "work as a developer by end of the year")
s8 = Student("Bituin Callanta", "Bituin[Gold]", "sashimi", "lessen the gender wage gap")



s1.my_print()
s2.my_print()
s3.my_print()
s4.my_print()
s5.my_print()
s6.my_print()
s7.my_print()
s8.my_print()

#Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.

class Student():
	def __init__(self, first_name, last_name, email, phone_num, github, country, gen_ident):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone_num = phone_num
		self.github = github
		self.country = country
		self. gen_ident = gen_ident

	def my_print(self):
		print(self.first_name + ", " + self.last_name + ", " + self.email + ", " + self.phone_num + ", " + self.github + ", " + self.country + ", " + self.gen_ident)

s1 = Student("Vanessa", "Stewart", "vs@madeup.com", "1-511-111-1111", "https://github.com/fakegithub", "USA", "female")

s1.my_print()

# ☼ Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?

# Humour is more diverse

