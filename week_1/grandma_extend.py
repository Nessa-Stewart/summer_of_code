import random

talk = ()
nbye = 0

while nbye < 3:
	talk = input("Say something to Granmda.")

	if talk =="BYE":
		print("I DIDN'T CATCH THAT!")
		nbye = (nbye +1)
		
	elif nbye == 3:
		print("SEE YOU LATER!")

	elif talk.isupper() == False:
		print("HUH?! SPEAK UP, GIRL!")
		nbye = 0
	else:
		print("NO, NOT SINCE" + " " + str(random.randint(1930,1950)) + "!")
		nbye = 0
	

	
	    





	    	