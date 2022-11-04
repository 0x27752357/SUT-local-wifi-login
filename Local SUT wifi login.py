import requests

URL = "http://wifi.shahroodut/login"

VALUES = {'username' : '40011573' ,
          'password' : '670952664'}
try :
        RESULT = requests.post(URL , VALUES)
        print("connected")
except :
        print("couldn't make connection with the server try again please !")
