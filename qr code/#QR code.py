#QR code 

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#make an input interface for the user 
import pyautogui
username=pyautogui.prompt(text='', title='username' , default='')
password=pyautogui.password(text='', title='password', default='', mask='*')
#name of user
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



