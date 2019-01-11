
# anne_niekrenz = dict(name = "Anne anne_niekrenz", discord_id = "anne", fav_food = "ice cream")

# print(anne_niekrenz)


# my_dict = {
# 	"a": 35000,
# 	"b": 8000,
# 	"z": 450
# }

# print(my_dict)

# #access

# print(my_dict["a"])

# #add

# my_dict["Rocio"] = "pretty"

# print(my_dict["Rocio"])

# print(my_dict)

# #modify

# my_dict["a"] = 50

# print(my_dict["a"])

# #delete item

# print(len(my_dict))

# del(my_dict["a"])

# print(my_dict)

# print(len(my_dict))

# #delete dictionary

# # del(my_dict)
# # print(my_dict)

#CLASSES

# class Student():
# 	discord_id = "virginia [Gold] [Volunteer]"

# #insantiate using our shiny new Constructor function that we for for 'free' from the Class
# s1 = Student()
# s2 = Student()
# s3 = Student()

# print(s1.discord_id)
# print(s2.discord_id)
# print(s3.discord_id)

class Student():
	def __init__(self, name, discord_id, fav_food, dream):
		self.name = name
		self.discord_id = discord_id
		self.fav_food = fav_food
		self.dream = dream

	def my_print(self):
		print(self.name + ", " + self.discord_id + ", " + self.fav_food + ", " + self.dream)


s1 = Student("Virginia Balsiro", "yesviginia [Gold] [Volunteer]", "pasta", "Moving to Europe")


s1.my_print()






