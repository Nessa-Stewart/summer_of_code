# for i in range(65, 65+2*32):
# 	if chr(i).isalpha():
# 		print(i, " stands for ", chr(i))


# def alphaprint():
# 	for i in range(65,123):
# 		if chr(i).isalpha():
# 			print(chr(i))

# alphaprint()

# message = input("Give me a message to cypher: ")

# cypher = []

# def cyphermaker(text):
# 	for c in text:
# 		cypher.append(ord(c))

# cyphermaker(message)

# print(cypher)


# M = 'M'
# o = 'o'
# world = [
#          [o,o,o,o,o,o,o,o,o,o,o],
#          [o,o,o,o,M,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,M,M,o],
#          [o,o,o,M,o,o,o,o,o,M,o],
#          [o,o,o,M,o,M,M,o,o,o,o],
#          [o,o,o,o,M,M,M,M,o,o,o],
#          [o,o,o,M,M,M,M,M,M,M,o],
#          [o,o,o,M,M,o,M,M,M,o,o],
#          [o,o,o,o,o,o,M,M,o,o,o],
#          [o,M,o,o,o,M,o,o,o,o,o],
#          [o,o,o,o,o,o,o,o,o,o,o]
#         ]

# def forwards():
# 	for i in world:
# 		print(*i)

# forwards()


M = 'M'
o = 'o'
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


# def backwards(L):
# 	L.reverse()
# 	for sublist in L:
# 		sublist.reverse()
# 	for i in reversed(L):
#           print(*i)


# backwards(world)

# def backwards():
# 	for i in world[::-1]:
# 		print(*i)

# backwards()

def backwards(L):
	for i in L[::-1]:
		[sublist[::-1] for sublist in L]
	print(*i)

backwards(world)



