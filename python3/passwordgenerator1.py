import easygui as e
import random as r


word=e.enterbox(msg="enter your password-word")
number=r.randint(1000,10000)
password=("{}{}".format(word,number))
e.msgbox(msg="your generated password is {}".format(password))
f=open("passwords.txt","a") # append, dranfügen
f.write("Password: {} \n".format(password))
f.close()    
e.msgbox("please check your new updated file passwords.txt")
