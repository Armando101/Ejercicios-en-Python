
def decimalToBinary(num):
	n=0
	stri = ""
	while True:
		stri += str(num%2)
		num=num//2
		if num == 0:
			return stri[::-1]

def binaryToDecimal(num):
	n=len(num)
	dec = 0
	for x in range(0,n):
		dec += int(num[n-1-x])*2**x
	return str(dec)

def decimalToHexadecimal(num):
	n = int(num)
	if n in range(0,10):
		return str(n)
	elif n == 10:
		return "A"
	elif n == 11:
		return "B"
	elif n == 12:
		return "C"
	elif n == 13:
		return "D"
	elif n == 14:
		return "E"
	elif n == 15:
		return "F"
	
def binaryToHexadecimal(num):
	stri = str(num)
	stri = stri[::-1]
	otraStr = ""
	n=0
	while True:
		auxStr = stri[4*n:4*(n+1):1]
		if auxStr == "":
			break
		auxStr=auxStr[::-1]
		otraStr += decimalToHexadecimal(binaryToDecimal(auxStr))
		n+=1
	otraStr=otraStr[::-1]
	return otraStr

listBinary=[]

for x in range(0,257):
	binary = decimalToBinary(x)
	print(binary)
	listBinary.append(int(binary))

for i in map(binaryToHexadecimal, listBinary):
	print(i)
