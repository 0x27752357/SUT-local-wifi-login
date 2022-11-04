import requests

URL = "http://wifi.shahroodut/login"

VALUES = {'username' : 'Your username' ,
          'password' : 'Your password'}
try :
        RESULT = requests.post(URL , VALUES)
        print("connected")
except :
        print("couldn't make connection with the server try again please !")
