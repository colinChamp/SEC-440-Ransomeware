# Import for symmetric encryption
from cryptography.fernet import Fernet

# Import for asymmetric encryption
import rsa

with open('asymPrivKey.pem', mode='rb') as privfile:
    keydata = privfile.read()
    asymPrivKey = rsa.PrivateKey.load_pkcs1(keydata)

symKeyFile = open("symKeyEnc.txt", "rb")
symKeyEnc = symKeyFile.read()

symKey = rsa.decrypt(symKeyEnc, asymPrivKey)

print(symKey)

fernet = Fernet(symKey)

ef = open("target.pwned", "rb")
encryptedFile = ef.read()

plainFile = fernet.decrypt(encryptedFile)

print(plainFile)
