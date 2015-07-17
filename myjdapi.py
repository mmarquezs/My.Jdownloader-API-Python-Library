import hashlib
import hmac
import requests
import json
import time
import urllib
import binascii
import base64
from Crypto.Cipher import AES
BS=16
pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
unpad = lambda s : s[0:-s[-1]]

class jddevice:
    """
    Class that represents a JD device and it's functions
    
    """
    def __init__(self,jd,deviceDict):
        """ This functions initializates the device instance.
        It uses the provided dictionary to create the device.

        :param deviceDict: Device dictionary
        
        """
        self.name=deviceDict["name"]
        self.dId=deviceDict["id"]
        self.dType=deviceDict["type"]
        self.jd=jd
    def addLinks(self,links,packageName,destinationFolder=False,extractPassword=False,autostart=False,priority="DEFAULT",downloadPassword=False):
        """
        Add links to the linkgrabber

        {
        "autostart" : false,
        "links" : null,
        "packageName" : null,
        "extractPassword" : null,
        "priority" : "DEFAULT",
        "downloadPassword" : null,
        "destinationFolder" : null
        }
        
        """
        links=",".join(links)
        params='{'
        if (links):
            params+='\\"links\\" : \\"'+links+'\\",'
        if (packageName):
            params+='\\"packageName\\" : \\"'+packageName+'\\",'
        if (extractPassword):
            params+='\\"extractPassword\\" : \\"'+extractPassword+'\\",'
        if (priority):
            params+='\\"priority\\" : \\"'+priority+'\\",'
        if (downloadPassword):
            params+='\\"downloadPassword\\" : \\"'+downloadPassword+'\\",'
        if (destinationFolder):
            params+='\\"destinationFolder\\" : \\"'+destinationFolder+'\\",'
        params+='\\"autostart\\" : '+str(autostart).lower()+','
        params=params[:-1]+"}"
        actionurl=self.__actionUrl()
        if not actionurl:
            return False
        text=self.jd.call(actionurl,"POST",rid=False,postparams=[params],action="/linkgrabberv2/addLinks")
        if not text:
            return False
    def queryLinks(self,bytesTotal=False,comment=False,status=False,enabled=False,maxResults=-1,startAt=0,packageUUIDs="null",host=False,url=False,availability=False,variantIcon=False,variantName=False,variantID=False,variants=False,priority=False):
        pass

    def __actionUrl(self):
        if not self.jd.sessiontoken:
            return False
        return "/t_"+self.jd.sessiontoken+"_"+self.dId


class myjdapi:
    """
    Main class for connecting to JD API.

    """
    
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
        self.loginSecret = False
        self.deviceSecret = False
        self.sessiontoken = False
        self.regaintoken = False
        self.serverEncryptionToken = False
        self.deviceEncryptionToken = False

        if email!=None and password!=None:
            self.connect(email,password)
            # Make an exception or something if it fails? Or simply ignore the error?
    def __secretcreate(self,email,password,domain):
        """Calculates the loginSecret and deviceSecret

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        :param domain: The domain , if is for Server (loginSecret) or Device (deviceSecret) 
        :return: secret hash

        """
        h = hashlib.sha256()
        h.update(email.lower().encode('utf-8')+password.encode('utf-8')+domain.lower().encode('utf-8'))
        secret=h.digest()
        return secret
    def __updateEncryptionTokens(self):
        """ 
        Updates the serverEncryptionToken and deviceEncryptionToken

        """
        if not self.serverEncryptionToken:
            oldtoken=self.loginSecret
        else:
            oldtoken=self.serverEncryptionToken            
        h = hashlib.sha256()
        h.update(oldtoken+bytearray.fromhex(self.sessiontoken))
        self.serverEncryptionToken=h.digest()
        h = hashlib.sha256()
        h.update(self.deviceSecret+bytearray.fromhex(self.sessiontoken))
        self.deviceEncryptionToken=h.digest()
    def __signaturecreate(self,key,data):
        """
        Calculates the signature for the data given a key.

        :param key: 
        :param data:

        """
        h = hmac.new(key,data.encode('utf-8'),hashlib.sha256)
        signature=h.hexdigest()
        return signature
    def __decrypt(self,secretServer,data):
        """
        Decrypts the data from the server using the provided token

        :param secretServer: 
        :param data:

        """
        iv=secretServer[:len(secretServer)//2]        
        key=secretServer[len(secretServer)//2:]
        decryptor = AES.new(key,AES.MODE_CBC,iv)
        decrypted_data = unpad(decryptor.decrypt(base64.b64decode(data)))
        return decrypted_data

    def __encrypt(self,secretServer,data):
        """
        Encrypts the data from the server using the provided token

        :param secretServer: 
        :param data:

        """
        data=pad(data.encode('utf-8'))
        iv=secretServer[:len(secretServer)//2]        
        key=secretServer[len(secretServer)//2:]
        encryptor = AES.new(key,AES.MODE_CBC,iv)
        encrypted_data = base64.b64encode(encryptor.encrypt(data))
        return encrypted_data.decode('utf-8')
    
    def __updateRid(self):
        """
        Adds 1 to rid
        """
        self.rid=int(time.time())
        #self.rid=self.rid+1
    def connect(self,email,password):
        """Establish connection to api

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        :returns: boolean -- True if succesful, False if there was any error.

        """
        self.loginSecret=self.__secretcreate(email,password,"server")
        self.deviceSecret=self.__secretcreate(email,password,"device")
        text=self.call("/my/connect","GET",rid=True,params=[("email",email),("appkey",self.appkey)])
        if not text:
            return False
        self.__updateRid()
        self.sessiontoken=text["sessiontoken"]
        self.regaintoken=text["regaintoken"]
        self.__updateEncryptionTokens()
        return True
    def reconnect(self):
        """
        Restablish connection to api.

        :returns: boolean -- True if succesful, False if there was any error.

        """
        if not self.sessiontoken:
            return False
        text=self.call("/my/reconnect","GET",rid=True,params=[("sessiontoken",self.sessiontoken),("regaintoken",self.regaintoken)])
        if not text:
            return False
        self.__updateRid()
        self.sessiontoken=text["sessiontoken"]
        self.regaintoken=text["regaintoken"]
        self.__updateEncryptionTokens()
        return True
    def disconnect(self):
        """
        Disconnects from  api

        :returns: boolean -- True if succesful, False if there was any error.

        """
        if not self.sessiontoken:
            return False
        text=self.call("/my/disconnect","GET",rid=True,params=[("sessiontoken",self.sessiontoken)])
        if not text:
            return False
        self.__updateRid()
        self.loginSecret = ""
        self.deviceSecret = ""
        self.sessiontoken = ""
        self.regaintoken = ""
        self.serverEncryptionToken = False
        self.deviceEncryptionToken = False
        return True

    def getDevices(self):
        """
        Gets available devices. Use listDevices() to get the devices list. 

        :returns: boolean -- True if succesful, False if there was any error.

        """
        if not self.sessiontoken:
            return False
        text=self.call("/my/listdevices","GET",rid=True,params=[("sessiontoken",self.sessiontoken)])
        if not text:
            return False
        self.__updateRid()
        self.__devices=text["list"]
        return True
    def listDevices(self):
        """
        Returns available devices. Use getDevices() to update the devices list. 

        Each device in the list is a dictionary like this example:
        
        { 
            'name': 'Device',

            'id': 'af9d03a21ddb917492dc1af8a6427f11',

            'type': 'jd'

        }

        :returns: list -- list of devices.

        """
        return self.__devices
    def getDevice(self,deviceid=False,name=False):
        """
        Returns a jddevice instance of the device
        
        :param deviceid:
        
        """
        if deviceid:
            for device in self.__devices:
                if device["id"]==deviceid:
                    return jddevice(self,device)
        elif name:
            for device in self.__devices:
                if device["name"]==name:
                    return jddevice(self,device)
        return False

    def call(self,url,httpaction="GET",rid=True,params=False,postparams=False,action=False):
        if not action:
            if (params):
                call=url
                for index,param in enumerate(params):
                    if index==0:
                        call+="?"+param[0]+"="+urllib.parse.quote(param[1])
                    else:
                        call+="&"+param[0]+"="+urllib.parse.quote(param[1])
                        # Todo : Add an exception if the param is loginSecret so it doesn't get url encoded.
                if rid:
                    call+="&rid="+str(self.rid)
            
                if not self.serverEncryptionToken:
                    call+="&signature="+str(self.__signaturecreate(self.loginSecret,call))
                else:
                    call+="&signature="+str(self.__signaturecreate(self.serverEncryptionToken,call))
            if (postparams):
                pass
        
        else:
            call=url+action
            if (params):
                
                for index,param in enumerate(params):
                    if index==0:
                        call+="?"+param[0]+"="+urllib.parse.quote(param[1])
                    else:
                        call+="&"+param[0]+"="+urllib.parse.quote(param[1])
                        # Todo : Add an exception if the param is loginSecret so it doesn't get url encoded.
                if rid:
                    call+="&rid="+str(self.rid)
            
                if not self.serverEncryptionToken:
                    call+="&signature="+str(self.__signaturecreate(self.loginSecret,call))
                else:
                    call+="&signature="+str(self.__signaturecreate(self.serverEncryptionToken,call))
            if (postparams):
                data='{"url":"'+action+'","params":["'
                print(postparams)
                for index,param in enumerate(postparams):
                    if index != len(postparams)-1:
                        data+=param+'","'
                    else:
                        data+=param+'"],'
            else:
                data='{"url":"'+action+'",'
            data+='"rid":'+str(self.rid)+',"apiVer":1}'
            print(data)
            encrypteddata=self.__encrypt(self.deviceEncryptionToken,data);

        url=self.api_url+call
        if httpaction=="GET":
            encryptedresp=requests.get(url)
        elif httpaction=="POST":
            print(encrypteddata)
            print(url)
            encryptedresp=requests.post(url,headers={"Content-Type": "application/aesjson-jd; charset=utf-8"},data=encrypteddata)

        print(encryptedresp.status_code)
        print(encryptedresp.text)
        if encryptedresp.status_code != 200:
            return False
        if not action:
            if not self.serverEncryptionToken:
                response=self.__decrypt(self.loginSecret,encryptedresp.text) 
            else:
                response=self.__decrypt(self.serverEncryptionToken,encryptedresp.text)
        else:
            response=self.__decrypt(self.deviceEncryptionToken,encryptedresp.text)
        jsondata=json.loads(response.decode('utf-8'))
        if jsondata['rid']!=self.rid:
            return False
        return jsondata

