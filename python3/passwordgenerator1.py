import easygui as e
import random as r

use=e.enterbox(msg="Enter the location (=application, website,..) where you want to use your password?")
word=e.enterbox(msg="enter your password-word")
number=r.randint(1000,10000)
password=("{}{}".format(word,number))
e.msgbox(msg="your generated password for {} is {}".format(use,password))
f=open("passwords.txt","a") # append, dranfügen
f.write("Use: {} Password: {} \n".format(use,password))
f.close()    
e.msgbox("please check your new updated file passwords.txt")
