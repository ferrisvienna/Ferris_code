#By ferrisofvienna

import easygui as e
import random as r
import time as t


alphabet="1","2"
use=e.enterbox(msg="Enter the location (=application, website,..) where you want to use your password?")
t.sleep (1/2)
word=e.enterbox(msg="enter your password-word")
number=r.randint(1000,10000)

password=("{}{}".format(word,number))
e.msgbox(msg="your generated password for {} is {}".format(use,password))
t.sleep(1/2)
f=open("passwords.txt","a") # append, dranfügen
f.write("Use: {} Password: {} \n".format(use,password))
f.close()    
t.sleep(1/2)
e.msgbox("please check your new updated file passwords.txt")
