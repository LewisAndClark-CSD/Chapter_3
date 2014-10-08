#Fortune_cookie
#dennis Gordick
#10/8/2014
import random
import time
cookie1="You should not take advice from a cookie."
cookie2="I am of no help to you."
cookie3="What am I, phsyic?" 
cookie4="Stop asking for more cookies, we are running out!"
cookie5="Ok, thats it. Get me out of your hand!"
cookie_list= [cookie1, cookie2, cookie3, cookie4, cookie5]
cookie=input("Do you want a cookie?")
while cookie=="yes":
    print("Let me get you one.")
    time.sleep(2.0)
    print(random.choice(cookie_list))
    cookie=input("Do you want another?")
