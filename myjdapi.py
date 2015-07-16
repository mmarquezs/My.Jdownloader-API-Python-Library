import hashlib
import hmac
import requests
import json
import time
import urllib
import binascii
import base64
from Crypto.Cipher import AES

unpad = lambda s : s[0:-s[-1]]

class myjdapi:

    def __init__(self,email=None,password=None):
        """ This functions initializates the myjdapi object.
        If email and password are given it will also connect try 
        with that account.
        If it fails to connect it won't provide any error,
        you can check if it worked by checking if sessiontoken 
        is not an empty string.
        
        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        
        """
        self.rid=int(time.time())
        self.api_url = "http://api.jdownloader.org"
        self.appkey = "http://git.io/vmcsk"
        self.apiVer = 1
        self.__devices = []
        self.loginSecret = ""
        self.deviceSecret = ""
        self.sessiontoken = ""
        self.regaintoken = ""
        self.serverEncryptionToken = ""
        self.deviceEncryptionToken = ""

        if email!=None and password!=None:
            self.connect(email,password)
            # Make an exception or something if it fails? Or simply ignore the error?    def __secretcreate(self,email,password,domain):
        # Calculate the loginSecret and deviceSecret
        # email,password, domain (server,device)
        h = hashlib.sha256()
        h.update(email.lower().encode('utf-8')+password.encode('utf-8')+domain.lower().encode('utf-8'))
        secret=h.digest()
        return secret
    def __updateEncryptionTokens(self):
        if self.serverEncryptionToken=='':
            oldtoken=self.loginSecret
        else:
            oldtoken=self.serverEncryptionToken            
        h = hashlib.sha256()
        h.update(oldtoken+bytearray.fromhex(self.sessiontoken))
        self.serverEncryptionToken=h.digest()
        h = hashlib.sha256()
        h.update(self.deviceSecret+self.sessiontoken.encode('utf-8'))
        self.deviceEncryptionToken=h.digest()
    def __signaturecreate(self,key,data):
        # Calculate the signature
        h = hmac.new(key,data.encode('utf-8'),hashlib.sha256)
        signature=h.hexdigest()
        return signature
    def __decrypt(self,secretServer,data):
        iv=secretServer[:len(secretServer)//2]        
        key=secretServer[len(secretServer)//2:]
        decryptor = AES.new(key,AES.MODE_CBC,iv)
        decrypted_data = unpad(decryptor.decrypt(base64.b64decode(data)))
        return decrypted_data
    def __updateRid(self):
        self.rid=int(time.time())
    def connect(self,email,password):
        # Establish connection to api
        self.loginSecret=self.__secretcreate(email,password,"server")
        self.deviceSecret=self.__secretcreate(email,password,"device")
        get="/my/connect?email="+urllib.parse.quote(email)+"&appkey="+urllib.parse.quote(self.appkey)+"&rid="+str(self.rid)
        get+="&signature="+str(self.__signaturecreate(self.loginSecret,get))
        url=self.api_url+get
        response=requests.get(url)
        if response.status_code != 200:
            return False
        text=self.__decrypt(self.loginSecret,response.text)
        jsondata=json.loads(text.decode('utf-8'))
        if jsondata['rid']!=self.rid:
            return False

        self.__updateRid()
        self.sessiontoken=jsondata["sessiontoken"]
        self.regaintoken=jsondata["regaintoken"]
        self.__updateEncryptionTokens()
        return True
    def reconnect(self):
        # Restablish connection to api
        get="/my/reconnect?sessiontoken="+self.sessiontoken+"&regaintoken="+self.regaintoken+"&rid="+str(self.rid)
        get+="&signature="+str(self.__signaturecreate(self.serverEncryptionToken,get))
        url=self.api_url+get

        response=requests.get(url)
        if response.status_code != 200:
            return False
        text=self.__decrypt(self.serverEncryptionToken,response.text)
        jsondata=json.loads(text.decode('utf-8'))

        if jsondata['rid']!=self.rid:
            return False
        self.__updateRid()
        self.sessiontoken=jsondata["sessiontoken"]
        self.regaintoken=jsondata["regaintoken"]
        self.__updateEncryptionTokens()
        return True
    def disconnect(self):
        # Disconnects from the api
        get="/my/disconnect?sessiontoken="+self.sessiontoken+"&rid="+str(self.rid)
        get+="&signature="+str(self.__signaturecreate(self.serverEncryptionToken,get))
        url=self.api_url+get

        response=requests.get(url)
        if response.status_code != 200:
            return False
        text=self.__decrypt(self.serverEncryptionToken,response.text)
        jsondata=json.loads(text.decode('utf-8'))

        if jsondata['rid']!=self.rid:
            return False
        self.__updateRid()
        return True
        # self.sessiontoken=jsondata["sessiontoken"]
        # self.regaintoken=jsondata["regaintoken"]
        # self.__updateEncryptionTokens()

    def getDevices(self):
        # Lists available devices.
        get="/my/listdevices?sessiontoken="+self.sessiontoken+"&rid="+str(self.rid)
        get+="&signature="+str(self.__signaturecreate(self.serverEncryptionToken,get))
        url=self.api_url+get
        response=requests.get(url)
        if response.status_code != 200:
            return False
        text=self.__decrypt(self.serverEncryptionToken,response.text)
        jsondata=json.loads(text.decode('utf-8'))
        print(jsondata)
        if jsondata['rid']!=self.rid:
            return False
        self.__updateRid()
        self.devices=jsondata["list"]
        return True


