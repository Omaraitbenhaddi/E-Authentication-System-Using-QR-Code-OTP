#QR code 

from datetime import datetime


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

#encrypt using RSA the info
import rsa
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('c:/Users/User/Documents/Project_cybersecurity/keys.publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('c:/Users/User/Documents/Project_cybersecurity/keys.privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('c:/Users/User/Documents/Project_cybersecurity/keys.publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('c:/Users/User/Documents/Project_cybersecurity/keys.privateKey.pem', 'rb') as p:
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
publicKey, privateKey =loadKeys()
ciphertext = encrypt(info, publicKey)
print("ciphertext :",ciphertext)
img=qrcode.make(ciphertext)
img.save("admin.png")
#save it in the user's pc


#authentication

#read the QRcode and decrypt the info
#to read QRCODE
import cv2
d=cv2.QRCodeDetector()

val,points,straight_qrcode=d.detectAndDecode(cv2.imread("admin.png"))
print(val)
#to decrypt
text = decrypt(ciphertext, privateKey)
print("plaintext:",text)
time_now = datetime.now()
date_now = time_now.strftime("%Y:%m:%d:%H:%M:%S").split(":")
auth_date = [ int(x) for x in date_now ]

if auth_date[3]<timing[3]+1:
    print("valid")
else:
    print("error")


