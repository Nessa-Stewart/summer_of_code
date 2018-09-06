items = []

while True:
    new_item = input("Please type any word (Hit enter key to quit): ")
	
    items.append(new_item)
	
    if new_item == "":
        break

        
print(sorted(items))
