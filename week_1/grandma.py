import random

talk = ()

while talk != "BYE":
	talk = input("Say something to Granmda.")
	if talk.isupper() == False:
		print("HUH?! SPEAK UP, GIRL!")
	else:
		print("NO, NOT SINCE" + str(random.randint(1930,1950)) + "!")
	


	    





	    	