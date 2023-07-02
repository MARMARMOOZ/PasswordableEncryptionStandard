from os import system
system("clear")
#the encrypt function for proccesing, Encrypting, Show.
def Encrypt(word, password):
	#Eword var, Encrypted word
	Eword = ""
	#Bword var, Beter word
	Bword = list(word)
	#char list, list of a,...0
	charlist = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]{};:'\"\\|,<.>/?1234567890=_+()*&^%$#@!~` ")
	#for(for detecting all chars in Bword)
	for i in range(len(Bword)):
		#li var, current word has it
		li = Bword[i]
		#rli var, has numerical char
		rli =  0
		#for(for detecting char in charlist and get numerical number)
		for j in range(len(charlist)):
			#check if this char in charlist[j]
			if charlist[j] ==  li:
				#save in rli
				rli = j
		#Encrypting
        #------------Here is alghoritm of encryption.
		rli = rli * (password * 808)
        #"* (pswd * 808)" its very simple i recomend you change it to a better thing.
		#saving rli to Eword with str format
		Eword += str(rli)
		#- for space
		Eword += "-"
	#returning the encrypted
	return Eword

#main

print("PES(1.0.0) Encrypter")
word = str(input("word:"))
password = int(input("password:"))
Eword = Encrypt(word, password)
print(f"Eword:{Eword}")
