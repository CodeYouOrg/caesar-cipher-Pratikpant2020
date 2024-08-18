#Alphabate are as below:
alphabate = "abcdefghijklmnopqrstuvwxyz"
#Number of place needed to shift right is 5
shift = 5
#Get input from user
ceaser_cipher = input("Please enter a sentence: ")
#If there is any upper case letter change them into lower case. 
ceaser_cipher = ceaser_cipher.lower()
#For now place enncrypted sentence as empty 
encrypted_sentence = ("")
#For every character in ceaser cipher
for char in ceaser_cipher:
    if char in alphabate:
#Get the index value as below 
        index = alphabate.find(char)
        index = (index + shift) - 26
#Get the char value
        char = alphabate[index]
#Finally encryptes sentence 

    encrypted_sentence += char
print(encrypted_sentence)
#Enter sentence "python is fun"
#output "udymts nx kzs"