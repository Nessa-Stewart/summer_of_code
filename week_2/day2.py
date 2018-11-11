#numbers to letters
for i in range(65, 65+2*32):
	if chr(i).isalpha():
		print(i, " stands for ", chr(i))

#fix the above so it prints only A-Z and a-z