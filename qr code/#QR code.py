#QR code 

#QR code 

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%Y:%m:%d:%H:%M:%S")
t = dt_string.split(':')
timing = [ int(x) for x in t ]

#make an input interface for the user 
import pyautogui
username=pyautogui.prompt(text='', title='username' , default='')
password=pyautogui.password(text='', title='password', default='', mask='*')
#name of user and password
user=username
passw=password

#to  generate QRCODE
import qrcode
info=user+" "+dt_string

#hash the info
import hashlib

hash_info=hashlib.sha256(info.encode('utf-8')).hexdigest()
img=qrcode.make(hash_info)
img.save("admin.png")
#save it in the user's pc

#authentication
time_now = datetime.now()
date_now = time_now.strftime("%Y:%m:%d:%H:%M:%S").split(":")
auth_date = [ int(x) for x in date_now ]

if auth_date[3]<timing[3]+1:
    print("valid")
else:
    print("error")
