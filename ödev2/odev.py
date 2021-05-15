file = open("odev.txt","r")
temiz = open("odev_temiz.txt","r+")

for line in file:
	for letter in line:
		if letter.isalpha()==True:
			temiz.write(letter)
	temiz.write("\n")