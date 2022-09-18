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

# key is generated
key = Fernet.generate_key()

# value of key is assigned to a variable
f = Fernet(key)

# the plaintext is converted to ciphertext
token = f.encrypt(info.encode())

print("ciphertext :",token)
img=qrcode.make(token)
img.save("user.png")
#save it in the user's pc


#authentication

#read the QRcode and decrypt the info
#to read QRCODE
import cv2
d=cv2.QRCodeDetector()

val,points,straight_qrcode=d.detectAndDecode(cv2.imread("user.png"))
print(val)

# decrypting the ciphertext
plaintext = f.decrypt(val.encode())

# display the plaintext
print(plaintext)

time_now = datetime.now()
date_now = time_now.strftime("%Y:%m:%d:%H:%M:%S").split(":")
auth_date = [ int(x) for x in date_now ]

if auth_date[3]<timing[3]+1:
    print("valid")
else:
    print("error")


