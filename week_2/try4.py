# class Student():
# 	def __init__(self, name, discord_id, fav_food, dream):
# 		self.name = name
# 		self.discord_id = discord_id
# 		self.fav_food = fav_food
# 		self.dream = dream

# 	def my_print(self):
# 		print(self.name + ", " + self.discord_id + ", " + self.fav_food + ", " + self.dream)


# s1 = Student("Virginia Balsiro", "yesviginia [Gold] [Volunteer]", "pasta", "Moving to Europe")
# s2 = Student("Andrea Visanoiu", "Andrea[Gold]", "wontonmee", "teaching university")
# s3 = Student("Cristina Tarantino", "CristyTarantino[Gold]", "pasta", " Being an amazing developer")
# s4 = Student("Deb Cupitt", "DebCupitt[Gold]", "chocolate", "Gender equality")
# s5 = Student("Marwa Qabell", "Marwa Qabeel[Gold]", "chocolate", "Data Analyst")
# s6 = Student("Sacha Young", "Sacha[Gold]", "french fries", "To return to research")
# s7 = Student("Jessica", "Jessi_RS[Gold]", "pasta", "work as a developer by end of the year")
# s8 = Student("Bituin Callanta", "Bituin[Gold]", "sashimi", "lessen the gender wage gap")



# s1.my_print()
# s2.my_print()
# s3.my_print()
# s4.my_print()
# s5.my_print()
# s6.my_print()
# s7.my_print()
# s8.my_print()


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