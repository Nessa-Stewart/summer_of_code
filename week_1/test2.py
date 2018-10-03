number = int(input("Enter number between 1 and 3000: "))

numerals = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))

def make_roman(number):
    result = ''
    for roman, n in numerals:
    	if n<= number:
    		result += roman * (number // n)
    		number %= n
    return result

print("Your Roman Numeral is " + make_roman(number) + ".")