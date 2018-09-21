#Day One------

#Hours in year

print('hours in a year',24 * 365)

#minutes in a decade

print('minutes in a decade', (((24*60)*365)*10))

#age in seconds

print('My age in seconds', ((((60*60)*24)*365)*38))

#Andreea's age as she figured

print("Andreea's age is ", 48618000/(((60*60)*24)*365))

#Andreas's age after it was corrected by multiplying by 24 to account for the mistake mentioned in the typos area

print("Andrea's age is",(48618000/(((60*60)*24)*365))*24)


#Day Three --------

#Full Name Greeting

first_name = input("What's your first name?")
middle_name = input("What's your middle name?")
last_name = input("What's your last name?")

print("Hello " + first_name + " " + middle_name + " " + last_name + "!")


#Bigger Better Favorite Number

user_number = int(input("What's your favorite number?"))

better_number = (user_number + 1)

print("I think that " + str(better_number) + " is superior to " + str(user_number))

#Angry Boss

want = input("What exactly do you want?!")

angry_want = want.upper()

print("WHADDAYA MEAN " + "'" + angry_want + "'" + "?1?" + "YOU'RE FIRED!!")

#Table of Contents

print("Table of Contents".ljust(40))

print("Chapter1".ljust(15) + "Getting Started".center(15) + "page 1".rjust(15))

print("Chapter2".ljust(15) + "Numbers".center(15) + "page 9".rjust(15))

print("Chapter3".ljust(15) + "Letters".center(15) + "page 13".rjust(15))

#random

import random

tile = ['x', 'o']

map = [] 


for i in range(11):
	for i in range(11):
		map.append(random.choice(tile))

print(map)

def countX(map, x):
	return map.count(x)

x = 'x'

print(countX(map, x))


#Day Four -----------

# 99 Bottles of Beer

for x in range(99, 0, -1):
    print(str(x) + " bottles of beer on the wall," + str(x) + " bottles of beer. Take one down and pass it around," +  str(x-1) + " bottles of beer on the wall.")


#Deaf Grandma

import random

talk = ()

while talk != "BYE":
	talk = input("Say something to Granmda.")
	if talk.isupper() == False:
		print("HUH?! SPEAK UP, GIRL!")
	else:
		print("NO, NOT SINCE" + str(random.randint(1930,1950)) + "!")
	

#Deaf Grandma extended

import random

talk = ()
nbye = 0

while nbye != 3:
	talk = input("Say something to Granmda.")

	if talk == "BYE":
		
		nbye = (nbye +1)
		if nbye == 3:
		  print("SEE  YOU LATER!")

	elif talk.isupper() == False:
		print("HUH?! SPEAK UP, GIRL!")
		nbye = 0
	else:
		print("NO, NOT SINCE" + " " + str(random.randint(1930,1950)) + "!")
		nbye = 0
	

#Leap Years


y1 = int(input("Please give me a year in xxxx format."))

y2 = int(input("Please give me a year in xxxx format."))



print("Leap years between " + str(y1) + " and " + str(y2) + " are:")

for i in range(y1, y2):
    if(i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print(str(i))    	
        

#Everday life calculation - Calculate kill/death ratio for last gaming session from user input

print("I can calculate your kill/death ratio for your last play session with your favorite video game.")

kills = int(input("Please tell me how many players you defeated in your last session: "))

deaths = int(input("Please tell me how many time you died in your last session: "))

kd = kills / deaths

print("Your kill/death reatio for your last play session was " + str(kd) + ".")	

#Building and sorting an array

items = []

while True:
    new_item = input("Please type any word (Hit enter key to quit): ")
	
    items.append(new_item)
	
    if new_item == "":
        break
items.pop()
print(sorted(items))

#Table of Contents

contents = {
	"chap-1" : {
	    "chapter" : "Chapter 1",
	    "name" : "Fancy Cats",
	    "page" : "1",
	},
	"chap_2" : {
	    "chapter" : "Chapter 2",
	    "name" : "Fat Cats",
	    "page" : "32",
	},
	"chap_3" : {
	    "chapter" : "Chapter 3",
	    "name" : "Hairless Cats",
	    "page" : "53",
	},
	"chap_4" : {
	    "chapter" : "Chapter 4",
	    "name" : "Fluffy Cats",
	    "page" : "75",
	},
}

for tbl_contents, cont_dict in contents.items():
	left = cont_dict["chapter"]
	middle = cont_dict["name"]
	right = cont_dict["page"]

	print(left.ljust(15) + middle.center(15) + right.rjust(15))
	




































