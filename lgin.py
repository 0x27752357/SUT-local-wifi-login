import requests

URL = "http://wifi.shahroodut/login"

VALUES = {'username' : 'TYPE YOUR USERNAME HERE' ,
          'password' : 'TYPE YOUR PASSWORD HERE'}
RESULT = requests.post(URL , VALUES)
print(RESULT.content)
