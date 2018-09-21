contents = {
	"chap-1" : {
	    "chapter" : "Chapter 1",
	    "name" : "Fancy Cats",
	    "page" : "1",
	},
	"chap_2" : {
	    "chapter" : "Chapter 2",
	    "name" : "Fat Cats",
	    "page" : "32",
	},
	"chap_3" : {
	    "chapter" : "Chapter 3",
	    "name" : "Hairless Cats",
	    "page" : "53",
	},
	"chap_4" : {
	    "chapter" : "Chapter 4",
	    "name" : "Fluffy Cats",
	    "page" : "75",
	},
}

for tbl_contents, cont_dict in contents.items():
	left = cont_dict["chapter"]
	middle = cont_dict["name"]
	right = cont_dict["page"]

	print(left.ljust(15) + middle.center(15) + right.rjust(15))
	