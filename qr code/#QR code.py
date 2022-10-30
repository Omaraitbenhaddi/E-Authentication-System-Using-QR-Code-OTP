#QR code 

from datetime import datetime
from encodings.utf_8 import encode


#make an input interface for the user 
import pyautogui
username=pyautogui.prompt(text='', title='username' , default='')
password=pyautogui.password(text='', title='password', default='', mask='*')
#name of user and password
user=username
passw=password

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%Y:%m:%d:%H:%M:%S")
t = dt_string.split(':')
timing = [ int(x) for x in t ]


#to  generate QRCODE
import qrcode
info=user+" "+dt_string

#encrypt using Fernet the info
# Fernet module is imported from the
# cryptography package
from cryptography.fernet import Fernet
import rsa
# key is generated
key = Fernet.generate_key()
#coding by RSA the key


def loadKeys():
    with open('./public key', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('./private key', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey

def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

generateKeys()
publicKey, privateKey =load_keys()


key_encypted = encrypt(key, publicKey)

#store the key_encrypted into your database

# value of key is assigned to a variable
f = Fernet(key)

# the plaintext is converted to ciphertext
token = f.encrypt(info.encode())

print("ciphertext :",token)
img=qrcode.make(token)
img.save("user.png")
#save it in the user's pc






