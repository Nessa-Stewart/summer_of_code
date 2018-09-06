
y1 = int(input("Please give me a year in xxxx format."))

y2 = int(input("Please give me a year in xxxx format."))



print("Leap years between " + str(y1) + " and " + str(y2) + " are:")

for i in range(y1, y2):
    if(i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print(str(i))    	
        


