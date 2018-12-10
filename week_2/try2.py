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


# M = 'M'
# o = '-'
# world = [
# 		 [o,o,o,o,o,o,o,o,o,o,o],
# 		 [o,o,o,o,M,M,o,o,o,o,o],
# 		 [o,o,o,o,o,o,o,o,M,M,o],
# 		 [o,o,o,M,o,o,o,o,o,M,o],
# 		 [o,o,o,M,o,M,M,o,o,o,o],
# 		 [o,o,o,o,M,M,M,M,o,o,o],
# 		 [o,o,o,M,M,M,M,M,M,M,o],
# 		 [o,o,o,M,M,o,M,M,M,o,o],
# 		 [o,o,o,o,o,o,M,M,o,o,o],
# 		 [o,M,o,o,o,M,o,o,o,o,o],
# 		 [o,o,o,o,o,o,o,o,o,o,o]
# 		]


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

# def backwards(L):
# 	for i in L[::-1]:
# 		[sublist[::-1] for sublist in L]
# 	print(*i)

# backwards(world)


# def reverse(world):
# 	world = [listElem[::-1] for listElem in world[::-1]]
# 	return world
# world = reverse(world)
# print(*world, sep = "\n")

# def reverse(world):
# 	world = [listElem[::-1] for listElem in world[::-1]]
# 	return world
	


# world = reverse(world)

# print('\n'.join(' '.join(str(cell) for cell in row) for row in world))

# print(*world)

# def reverse(world):
# 	mutatedList = []
# 	for i in world:
# 		i.reverse()
# 		mutatedList.append(i)
# 	mutatedList.reverse()
# 	world = mutatedList[:]
# 	# print(world)
# reverse(world)
# # print(*world, sep='\n')
# print('\n'.join(' '.join(str(cell) for cell in row) for row in world))

# M = 'M'
# o = '-'
# world = [
# 		 [o,o,o,o,o,o,o,o,o,o,o],
# 		 [o,o,o,o,M,M,o,o,o,o,o],
# 		 [o,o,o,o,o,o,o,o,M,M,o],
# 		 [o,o,o,M,o,o,o,o,o,M,o],
# 		 [o,o,o,M,o,M,M,o,o,o,o],
# 		 [o,o,o,o,M,M,M,M,o,o,o],
# 		 [o,o,o,M,M,M,M,M,M,M,M],
# 		 [o,o,o,M,M,o,M,M,M,o,o],
# 		 [o,o,o,o,o,o,M,M,o,o,o],
# 		 [o,M,o,o,o,M,o,o,o,o,o],
# 		 [o,o,o,o,o,o,o,o,o,o,o]
# 		]



# def continent_counter(world, x, y):
# 	if(x>10 or x<0) or (y>10 or y<0):
# 		return 0
# 	if world[y][x] != 'M':
# 	# Either it's water or we already counter it,
# 	# but wither way, we don't want to count it now.
# 		return 0

# 	#So firest we count this tile....
# 	size = 1
# 	world[y][x] = 'counted land'
# 	#...then we count all of the neighboring eight tiles
# 	#(and, of course, their neighbors by way of the recursion).

# 	size = size + continent_counter(world, x-1,y-1)
# 	size = size + continent_counter(world, x, y-1)
# 	size = size + continent_counter(world, x+1, y-1)
# 	size = size + continent_counter(world, x-1, y )
# 	size = size + continent_counter(world, x+1, y )
# 	size = size + continent_counter(world, x-1, y+1)
# 	size = size + continent_counter(world, x , y+1)
# 	size = size + continent_counter(world, x+1, y+1)
# 	return size

# print(continent_counter(world, 5,5))



import random

tile = ['-', 'M']

board = []


# for i in range(5):
# 	map.append(random.choice(tile))
# 	for i in range(5):
# 		map.append(random.choice(tile))

# map = ' '.join(map)

# print(map)





# print(map, sep ="\n")

# def generate(n):
# 	return[map.append(random.choice(tile))for i in range(n) for j in range(n)]

# generate(20)


# print(*map)

def generate(rows, cols):
	return[board.append(random.choice(tile))for i in range(cols) for j in range(rows)]

generate(5, 5)


# print(*map)

# map = ' '.join(map)

# print(*map)

print('\n'.join(map(str, board)))

