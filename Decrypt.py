from os import system
system("clear")
#the decrypt function for proccesing, decrypting, Show.
def Decrypt(Eword, password):
	#word var, saving result
	word = ""
	#BEword var, beter Eword
	BEword = list(Eword)
	#char list
	charlist = list("ضصثقفغعهخحشسیبلاتنمکگظطزرذدپqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]{};:'\"\\|,<.>/?1234567890=_+()*&^%$#@!~` ")
	#token var, lexer char saving in this
	token = ""
	#for(lexer)
	for i in range(len(Eword)):
		#if current char is - ...
		if BEword[i] == "-":
			#saving the current token to ie
			ie = int(token)
			#Encrypting
            #----------for changing the alghoritm of encryption you need change there.
			DN = (ie) / (password * 808)
			#add word the char of the number
			word += charlist[int(DN%len(charlist))]
			#clear token
			token = ""
		#if current char is'n - ...
		elif BEword[i] != "-":
			#add char to token
			token += BEword[i]
	#returnnig the word
	return word

#main

print("PES(1.0.0) Decrypter")
Eword = str(input("Eword:"))
password = int(input("password:"))
word = Decrypt(Eword, password)
print(f"word:{word}")
