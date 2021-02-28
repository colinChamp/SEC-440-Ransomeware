# Import for symmetric encryption
from cryptography.fernet import Fernet

# Import for asymmetric encryption
import rsa

with open('asymPrivKey.pem', mode='rb') as privfile:
    keydata = privfile.read()
    asymPrivKey = rsa.PrivateKey.load_pkcs1(keydata)

symKeyFile = open("symKeyEnc.txt", "r")
    
symKey = rsa.decrypt(symKeyFile, asymPrivKey)

fernet = Fernet(symKey)

ef = open("target.pwned", "r")

plainFile = fernet.decrypt(ef)

print(plainFile)
