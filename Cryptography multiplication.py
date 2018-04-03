# ord("a") = ASCII num
# chr(numer) = letter

# "Encrypts" a message by multiplying it with a key

savetofile = True  # whether or not to use a text file for input/output
'''
Set to True for long texts like emails
Set to False for short sms like texts
'''


def encrypt(message, key):
    ASCIImessage = ""
    ASCIIkey = ""

    for scanningLetter in message:  # encoding message in ASCII
        ASCIIencodedLetter = ""
        ASCIIencodedLetter = ASCIIencodedLetter + str(ord(scanningLetter))
        if int(ASCIIencodedLetter) < 100:
            ASCIIencodedLetter = str(0) + str(ASCIIencodedLetter)
        ASCIImessage = ASCIImessage + str(ASCIIencodedLetter)
        del ASCIIencodedLetter

    if int(ASCIImessage[0]) == 0:  # add a { (ASCII:123) to handle the 0 at the beginning
        ASCIImessage = str(ord("{")) + ASCIImessage

    #############################################################

    for scanningLetter in key:  # encoding key in ASCII
        ASCIIencodedLetter = ""
        ASCIIencodedLetter = ASCIIencodedLetter + str(ord(scanningLetter))
        if int(ASCIIencodedLetter) < 100:
            ASCIIencodedLetter = str(0) + str(ASCIIencodedLetter)
        ASCIIkey = ASCIIkey + str(ASCIIencodedLetter)
        del ASCIIencodedLetter

    if int(ASCIIkey[0]) == 0:  # add a { (ASCII:123) to handle the 0 at the beginning
        ASCIIkey = str(ord("{")) + ASCIIkey

    output = int(ASCIImessage) * int(ASCIIkey)  # encrypting message with key

    if savetofile:
        return str(output)
    else:
        print("Encrypted message: " + str(output))


def decrypt(encryptedmessage, key):
    ASCIIkey = ""
    message = ""

    for scanningLetter in key:  # encoding key in ASCII
        ASCIIencodedLetter = ""
        ASCIIencodedLetter = ASCIIencodedLetter + str(ord(scanningLetter))
        if int(ASCIIencodedLetter) < 100:
            ASCIIencodedLetter = str(0) + str(ASCIIencodedLetter)
        ASCIIkey = ASCIIkey + str(ASCIIencodedLetter)
        del ASCIIencodedLetter

    if int(ASCIIkey[0]) == 0:  # add a { (ASCII:123) to remove the 0 at the beginning
        ASCIIkey = str(ord("{")) + ASCIIkey

    ASCIImessage = int(encryptedmessage) // int(ASCIIkey)  # decrypting

    ##############################################################

    scanningLetterPasses = 0
    ASCII3letters = ""
    chrLetter = ""

    for scanningLetter in str(ASCIImessage):  # decoding message to unicode
        scanningLetterPasses += 1
        ASCII3letters = str(ASCII3letters) + str(scanningLetter)

        if scanningLetterPasses % 3 == 0:
            # print(ASCII3letters)
            try:
                chrLetter = str(chrLetter) + chr(int(ASCII3letters))  # check if 0 is in the beginning
            except SyntaxError:
                chrLetter = str(chrLetter)[1:]  # remove it
                chrLetter = str(chrLetter) + chr(int(ASCII3letters))
            except ValueError:  # check if ASCII3letters is empty, in that case do nothing
                pass
            message = str(message) + chrLetter
            chrLetter = ""
            ASCII3letters = ""
    if ord(message[0]) == 123:  # remove the character that was used to handle the 0
        message = message[1:]

    if savetofile:
        return str(message)
    else:
        print("Message: " + str(message))


def ASCIItable():
    x = 33  # beginning 33 // end 170
    while 33 <= x <= 127:
        print("ASCII: " + str(x) + " Unicode: " + chr(x))
        x += 1


if savetofile:
    print(
        "[WARNING]: This program will create and modify files with the following names: \nmessage.txt, "
        "encryptedMessage.txt, decryptedMessage.txt !!!")

while True:
    userChoice = input("\nType 1 to encrypt\nType 2 to decrypt\nType 3 to display ASCII table\n")
    try:  # handle error if user enters non int character
        if int(userChoice) == 1:  # encrypt
            if savetofile:
                try:
                    fileMessage = open("message.txt", "r")
                    print("Found message.txt file")
                except FileNotFoundError:
                    fileMessage = open("message.txt", "w+")  # create an empty file
                    fileMessage.close()  # close file
                    input("Please enter and save the message you wish to encrypt in message.txt\nPress enter when done")
                    fileMessage = open("message.txt", "r")  # reopen file in read mode
                userPW = input("Enter the key to encrypt your message with: ")
                userMessage = fileMessage.read()
                fileMessage.close()
                if userMessage is not "" and userPW is not "":
                    encryptedMessage = open("encryptedMessage.txt", "w+")
                    encryptedMessage.write(encrypt(userMessage, userPW))
                    encryptedMessage.close()
                    print("The encrypted message has been saved to encryptedMessage.txt!")
                if userMessage is "" or userPW is "":
                    print("Please make sure message.txt contains some text and that you entered a key.")
            else:
                userMessage = input("Enter the message to encrypt: ")
                userPW = input("Enter the key to encrypt your message with: ")
                if userMessage is not "" and userPW is not "":
                    encrypt(userMessage, userPW)
                if userMessage is "" or userPW is "":
                    print("Please make sure you entered the message and key.")
                del userMessage, userPW
        if int(userChoice) == 2:  # decrypt ###############################################
            if savetofile:
                try:
                    encryptedMessage = open("encryptedMessage.txt", "r")
                    print("Found encryptedMessage.txt!")
                except FileNotFoundError:
                    encryptedMessage = open("encryptedMessage.txt", "w+")
                    encryptedMessage.close()
                    input("Please enter and save the encrypted message you wish to decrypt in encryptedMessage.txt\n"
                          "Press enter when done")
                    encryptedMessage = open("encryptedMessage.txt", "r")
                userPW = input("Enter the key to decrypt your message with: ")
                userMessage = encryptedMessage.read()
                encryptedMessage.close()
                if userMessage is not "" and userPW is not "":
                    decryptedMessage = open("decryptedMessage.txt", "w+",
                                            encoding='utf-8')  # utf-8 encoding to support non ascii characters if the password entered is wrong
                    decryptedMessage.write(decrypt(userMessage, userPW))
                    decryptedMessage.close()
                    print("The decrypted message has been saved to decryptedMessage.txt!")
                if userMessage is "" or userPW is "":
                    print("Please make sure you entered the encrypted message in encryptedMessage.txt and a key.")
            else:
                userMessage = input("Enter the encrypted message: ")
                userPW = input("Enter the key to decrypt your message with: ")
                if userMessage is not "" and userPW is not "":
                    decrypt(userMessage, userPW)
                if userMessage is "" or userPW is "":
                    print("Please make sure you entered the message and key.")
                del userMessage, userPW
        if int(userChoice) == 3:  # ASCII table
            ASCIItable()
        else:
            pass
    except ValueError:  # do nothing if user enters non int character
        pass
