#QR code 

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


#name of user
user="admin"
#to  generate QRCODE
import qrcode
info=user+" "+dt_string

#hash the info
import hashlib

hash_info=hashlib.sha256(info.encode('utf-8')).hexdigest()
img=qrcode.make(hash_info)
img.save("admin.png")

#to read QRCODE
import cv2
d=cv2.QRCodeDetector()

val,points,straight_qrcode=d.detectAndDecode(cv2.imread("admin.png"))

print(val)

#OTP_generator
# import library
import math, random
 
# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
 
# Driver code
if __name__ == "__main__" :
     
    print("OTP of 4 digits:", generateOTP())