number = int(input("Enter number between 1 and 3000: "))

numerals = (("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1))

def make_roman(number):
    result = ''
    for roman, n in numerals:
    	if n<= number:
    		result += roman * (number // n)
    		number %= n
    return result

make_roman(number) 