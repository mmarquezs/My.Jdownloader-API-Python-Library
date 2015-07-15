import hashlib
import hmac
import requests
import json
import time
import urllib
import base64
from Crypto.Cipher import AES

unpad = lambda s : s[0:-ord(s[-1])]

class myjdapi:

    def __init__(self,email=None,password=None):
        self.rid_counter=int(time.time())
        self.api_url = "http://api.jdownloader.org"
        self.appkey = "http://git.io/vmcsk"
        self.apiVer = 1
        self.devices = []
        self.loginSecret = ""
        self.deviceSecret = ""
        self.sessiontoken = ""
        self.regaintoken = ""
        self.serverEncryptionToken = ""
        self.deviceEncryptionToken = ""

        if email!=None and password!=None:
            self.connect(email,password)
    def __secretcreate(self,email,password,domain):
        # Calculate the loginSecret and deviceSecret
        # email,password, domain (server,device)
        h = hashlib.sha256()
        h.update(email.lower().encode('utf-8')+password.encode('utf-8')+domain.lower().encode('utf-8'))
        secret=h.digest()
        return secret
    def __signaturecreate(self,key,data):
        # Calculate the signature
        h = hmac.new(key,data.encode('utf-8'),hashlib.sha256)
        signature=h.hexdigest()
        return signature
    def __decrypt(self,secretServer,data):
        print ("secretServer: ",str(secretServer))
        iv=secretServer[:int(len(secretServer)/2)]
        print("IV: "+str(iv))
        
        key=secretServer[int(len(secretServer)/2):]
        print("Key: "+str(key))
        decryptor = AES.new(key,AES.MODE_CBC,iv)
        decrypted_data = unpad(decryptor.decrypt(base64.b64decode(data)))
        return decrypted_data
    def connect(self,email,password):
        # Establish connection to api
        self.loginSecret=self.__secretcreate(email,password,"server")
        self.deviceSecret=self.__secretcreate(email,password,"device")
        url=self.api_url+"/my/connect"
        get="/my/connect?email="+urllib.parse.quote(email)+"&appkey="+urllib.parse.quote(self.appkey)+"&rid="+str(self.rid_counter)
        get+="&signature="+str(self.__signaturecreate(self.loginSecret,get))
        url=self.api_url+get
        response=requests.get(url)
        print(response.status_code)
        print(url)
        print(response.text)
        if response.status_code != 200:
            return False
        print(str(response.text))
        text=self.__decrypt(self.loginSecret,response.text)
        print(str(text))
        jsondata=json.loads(text)
        if jsondata['rid']!=self.rid_counter:
            return False
        print(url)
        print(text)
        
            
    def reconnect(email,password):
        # Restablish connection to api
        pass
    def disconnect(email,password):
        # Restablish connection to api
        pass
    def devices():
        # Lists available devices.
        pass


