# Calculate a table for each letter in the alphabet from a-z, and count how many times each 
#letter appears in Alcie in Wonderland (fancy word for counting stuff is "frequency distribution" 
#-because you are counting the frquency of something)


filename = "alice_in_wonderland.txt"
file = open(filename, "r")

alphabets = "abcdefghijklmnopqrstuvwxyz"

raw = file.read()

raw.count(alphabets)
	
