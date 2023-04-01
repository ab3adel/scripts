from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

user_name = 'mohammad'
password = '123456'
arr=['bird','coin','desk','pc','camera','chair','meadow','siege','play','rose','girl','car']

key =user_name+password
salt =os.urand
kdf =P
def crypt (arr) :
    fernet=Fernet(key.encode())
    new_arr= []
    for i in arr:
        new_arr.push(fernet.encrypt(i.encode()))
    with open('crypto.txt','w') as f :
        f.write(new_arr)
crypt(arr)        