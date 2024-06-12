import os
import math
import random
import smtplib

digits = "1234567890"
OTP = ""
for i in range(6):
    OTP += digits[random.randint(0, 9)]

otp = OTP + " is your OTP"
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("your email id", "your password")

emailid = input("Enter your email id: ")
s.sendmail('&&&&&&&&&&&', emailid, msg)

a = input("Enter the OTP: ")
if a == OTP:
    print("Verified")
else:
    print("Not Verified")
