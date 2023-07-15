#Vivianne Everington

def encode(password):
	encoded_password = ""
	for digit in password:
		encoded_digit = str(int(digit) + 3)
		encoded_password += encoded_digit
	return encoded_password

if __name__ == "__main__":
	while True:
		print("\nMenu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit\n")

		option = input("Please enter an option: ")

		if option == "1":
			pswd = input("Please enter your password to encode: ")
			encoded_pswd = encode(pswd)
			print("Your password has been encoded and stored!")

		elif option == "2":
			print("The encoded password is " + encoded_pswd + " and the original password is " + pswd + ".")

		elif option == "3":
			exit()
