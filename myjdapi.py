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

class linkgrabber:
    """
    Class that represents the linkgrabber of a Device
    """
    def __init__(self,device):
        self.device=device
    
    

    def setEnabled(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass
    
    def getVariants(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass
    
    def queryLinks(self,params=[{"bytesTotal" : False,"comment" : False,"status" : False,"enabled" : False, "maxResults" : -1,"startAt" : 0,"packageUUIDs" : False,"host" : False,"url" : False,"availability" : False,"variantIcon" : False,"variantName" : False,"variantID" : False,"variants" : False,"priority" : False}]):
        """
        Get the links in the linkcollector
        
        {
        "bytesTotal"    : false,
        "comment"       : false,
        "status"        : false,
        "enabled"       : false,
        "maxResults"    : false,
        "startAt"       : false,
        "packageUUIDs"  : false,
        "hosts"         : false,
        "url"           : false,
        "availability"  : false,
        "variantIcon"   : false,
        "variantName"   : false,
        "variantID"     : false,
        "variants"      : false,
        "priority"      : false
        }
        """
        resp=self.action("/linkgrabberv2/queryLinks",postparams=params)
        self.jd.updateRid()
        return resp
    def moveToDownloadlist(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    
    def addLinks(self,params=[{"autostart" : False,"links" : "","packageName" : "","extractPassword" : "","priority" : "DEFAULT","downloadPassword" : "","destinationFolder" : ""}]):
        """
        Add links to the linkcollector

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
        resp=self.device.action("/linkgrabberv2/addLinks",postparams=params)
        self.jd.updateRid()
        return resp

    def addContainer(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    
    def getchildrenchanged(self):
        """
        no idea what parameters i have to pass and/or i don't know what it does.
        if i find out i will implement it :p
        """
        pass


    def setPriority(self):
        """
        no idea what parameters i have to pass and/or i don't know what it does.
        if i find out i will implement it :p
        """
        pass

    def removeLinks(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass
    
    def getDownloadFolderHistorySelectionBase(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass
    
    def help(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass
    
    def renameLink(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass
    
    def moveLinks(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def setVariant(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def getPackageCount(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass
    
 class downloads:
    """
    Class that represents the downloads list of a Device
    """
    def __init__(self,device):
        self.device=device
    
      
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
        self.linkgrabber=linkgrabber(self)
        self.downloads=downloads(self)
    def action(self,action=False,params=False,postparams=False):
        """
        Execute any action in the device using the postparams and params.
        
        All the info of which params are required and what are they default value, type,etc 
        can be found in the MY.Jdownloader API Specifications ( https://goo.gl/pkJ9d1 ).


        :param params: Params in the url, in a list of tuples. Example: /example?param1=ex&param2=ex2 [("param1","ex"),("param2","ex2")]
        :param postparams: List of Params that are send in the post. 

        
        """
        if not action:
            return False
        httpaction="POST"
        actionurl=self.__actionUrl()
        if not actionurl:
            return False
        if postparams:
            post=[]
            for postparam in postparams:
                if type(postparam)==type({}):
                    keys=list(postparam.keys())
                    data="{"
                    for param in keys:
                        if type(postparam[param])==bool:
                            data+='\\"'+param+'\\" : '+str(postparam[param]).lower()+','
                        elif type(postparam[param])==str:
                            data+='\\"'+param+'\\" : \\"'+postparam[param]+'\\",'
                        else:
                            data+='\\"'+param+'\\" : '+str(postparam[param])+','
                    data=data[:-1]+"}"
                else:
                    data=postparam
                post+=[data]
            if not params:
                text=self.jd.call(actionurl,httpaction,rid=False,postparams=post,action=action)
            else:
                text=self.jd.call(actionurl,httpaction,rid=False,params=params,postparams=post,action=action)
        else:
            text=self.jd.call(actionurl,httpaction,rid=False,action=True)
        if not text:
            return False
        return True
    
       
    
    # def queryLinksLinkcollector(self,bytesTotal=False,comment=False,status=False,enabled=False,maxResults=-1,startAt=0,packageUUIDs=False,host=False,url=False,availability=False,variantIcon=False,variantName=False,variantID=False,variants=False,priority=False):
    #     """
    #     Get the links in the linkcollector
        
    #     """
    #     params='{'
    #     if (bytesTotal):
    #         params+='\\"bytesTotal\\" : \\"'+str(bytesTotal).lower()+'\\",'
    #     if (comment):
    #         params+='\\"comment\\" : \\"'+str(comment).lower()+'\\",'
    #     if (status):
    #         params+='\\"status\\" : \\"'+str(extractPassword).lower()+'\\",'
    #     if (enabled):
    #         params+='\\"enabled\\" : \\"'+str(enabled).lower()+'\\",'
    #     params+='\\"maxResults\\" : \\"'+str(maxResults)+'\\",'
    #     params+='\\"startAT\\" : \\"'+str(startAt)+'\\",'
    #     if (packageUUIDs):
    #         params+='\\"packageUUIDs\\" : \\"'+packageUUIDs+'\\",'
    #     if (host):
    #         params+='\\"host\\" : \\"'+str(host).lower()+'\\",'
    #     if (url):
    #         params+='\\"url\\" : \\"'+str(url).lower()+'\\",'
    #     if (availability):
    #         params+='\\"availability\\" : \\"'+str(availability).lower()+'\\",'
    #     if (variantIcon):
    #         params+='\\"variantIcon\\" : \\"'+str(variantIcon).lower()+'\\",'
    #     if (variantName):
    #         params+='\\"variantName\\" : \\"'+str(variantName).lower()+'\\",'
    #     if (variantID):
    #         params+='\\"variantID\\" : \\"'+str(variantID).lower()+'\\",'
    #     if (variants):
    #         params+='\\"variants\\" : \\"'+str(variants).lower()+'\\",'
    #     if (priority):
    #         params+='\\"priority\\" : \\"'+str(priority).lower()+'\\",'
    #     params=params[:-1]+"}"
    #     actionurl=self.__actionUrl()
    #     if not actionurl:
    #         return False
    #     text=self.jd.call(actionurl,"POST",rid=False,postparams=[params],action="/linkgrabberv2/queryLinks")
    #     if not text:
    #         return False
    #     print(text)
    #     self.jd.updateRid()
    def queryLinksDownloadsList(self,params=[{"bytesTotal" : False, "comment" : False, "status" : False, "enabled" : False, "maxResults" : -1, "startAt" : 0, "packageUUIDs" : False, "host" : False, "url" : False, "bytesloaded" : False, "speed" : False, "eta" : False, "finished" : False, "priority" : False, "running" : False, "skipped" : False, "extractionStatus" : False}]):
        """
        Get the links in the downloadlist
        """

        resp=self.action("/downloadsV2/queryLinks",postparams=params)
        self.jd.updateRid()
        return resp
    # def queryLinksDownloads(self,bytesTotal=False,comment=False,status=False,enabled=False,maxResults=-1,startAt=0,packageUUIDs=False,host=False,url=False,bytesLoaded=False,speed=False,eta=False,finished=False,priority=False,running=False,skipped=False,extractionStatus=False):
    #     """
    #     Get the links in the downloadlist
        
    #     """
    #     params='{'
    #     if (bytesTotal):
    #         params+='\\"bytesTotal\\" : \\"'+str(bytesTotal).lower()+'\\",'
    #     if (comment):
    #         params+='\\"comment\\" : \\"'+str(comment).lower()+'\\",'
    #     if (status):
    #         params+='\\"status\\" : \\"'+str(extractPassword).lower()+'\\",'
    #     if (enabled):
    #         params+='\\"enabled\\" : \\"'+str(enabled).lower()+'\\",'
    #     params+='\\"maxResults\\" : \\"'+str(maxResults)+'\\",'
    #     params+='\\"startAT\\" : \\"'+str(startAt)+'\\",'
    #     if (packageUUIDs):
    #         params+='\\"packageUUIDs\\" : \\"'+packageUUIDs+'\\",'
    #     if (host):
    #         params+='\\"host\\" : \\"'+str(host).lower()+'\\",'
    #     if (url):
    #         params+='\\"url\\" : \\"'+str(url).lower()+'\\",'
    #     if (bytesLoaded):
    #         params+='\\"bytesLoaded\\" : \\"'+str(bytesLoaded).lower()+'\\",'
    #     if (speed):
    #         params+='\\"speed\\" : \\"'+str(speed).lower()+'\\",'
    #     if (eta):
    #         params+='\\"eta\\" : \\"'+str(eta).lower()+'\\",'
    #     if (finished):
    #         params+='\\"finished\\" : \\"'+str(finished).lower()+'\\",'
    #     if (priority):
    #         params+='\\"priority\\" : \\"'+str(priority).lower()+'\\",'
    #     if (running):
    #         params+='\\"running\\" : \\"'+str(running).lower()+'\\",'
    #     if (skipped):
    #         params+='\\"skipped\\" : \\"'+str(skipped).lower()+'\\",'
    #     if (extractionStatus):
    #         params+='\\"extractionStatus\\" : \\"'+str(extractionStatus).lower()+'\\",'
    #     params=params[:-1]+"}"
    #     actionurl=self.__actionUrl()
    #     if not actionurl:
    #         return False
    #     text=self.jd.call(actionurl,"POST",rid=False,postparams=[params],action="/downloadsV2/queryLinks")
    #     if not text:
    #         return False
    #     print(text)
    #     self.jd.updateRid()

    # def queryPackagesDownloads(self,bytesTotal=False,comment=False,status=False,enabled=False,maxResults=-1,startAt=0,packageUUIDs=False,childCount=False,hosts=False,saveTo=False,availableOfflineCount=False,availableOnlineCount=False,availableTempUnknownCount=False,availableUnknownCount=False):
    #     """
    #     Get the links in the downloadlist
        
    #     """
    #     params='{'
    #     if (bytesTotal):
    #         params+='\\"bytesTotal\\" : \\"'+str(bytesTotal).lower()+'\\",'
    #     if (comment):
    #         params+='\\"comment\\" : \\"'+str(comment).lower()+'\\",'
    #     if (status):
    #         params+='\\"status\\" : \\"'+str(extractPassword).lower()+'\\",'
    #     if (enabled):
    #         params+='\\"enabled\\" : \\"'+str(enabled).lower()+'\\",'
    #     params+='\\"maxResults\\" : \\"'+str(maxResults)+'\\",'
    #     params+='\\"startAT\\" : \\"'+str(startAt)+'\\",'
    #     if (packageUUIDs):
    #         params+='\\"packageUUIDs\\" : \\"'+packageUUIDs+'\\",'
    #     if (hosts):
    #         params+='\\"hosts\\" : \\"'+str(hosts).lower()+'\\",'
    #     if (saveTo):
    #         params+='\\"saveTo\\" : \\"'+str(saveTo).lower()+'\\",'
    #     if (availableOfflineCount):
    #         params+='\\"availableOfflineCount\\" : \\"'+str(availableOfflineCount).lower()+'\\",'
    #     if (availableOnlineCount):
    #         params+='\\"availableOnlineCount\\" : \\"'+str(availableOnlineCount).lower()+'\\",'
    #     if (availableTempUnknownCount):
    #         params+='\\"availableTempUnknownCount\\" : \\"'+str(availableTempUnknownCount).lower()+'\\",'
    #     if (availableUnknownCount):
    #         params+='\\"availableUnknownCount\\" : \\"'+str(availableUnknownCount).lower()+'\\",'
    #     params=params[:-1]+"}"
    #     actionurl=self.__actionUrl()
    #     if not actionurl:
    #         return False
    #     text=self.jd.call(actionurl,"POST",rid=False,postparams=[params],action="/downloadsV2/queryPackages")
    #     if not text:
    #         return False
    #     print(text)
    #     self.jd.updateRid()

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
    
    def updateRid(self):
        """
        Updates Rid
        """
        self.rid=int(time.time())
    def connect(self,email,password):
        """Establish connection to api

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        :returns: boolean -- True if succesful, False if there was any error.
        
        TODO: Add token parameters so it can connect without using email and password,set tokens and then connect. 
        """
        self.loginSecret=self.__secretcreate(email,password,"server")
        self.deviceSecret=self.__secretcreate(email,password,"device")
        text=self.call("/my/connect","GET",rid=True,params=[("email",email),("appkey",self.appkey)])
        if not text:
            return False
        self.updateRid()
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
        self.updateRid()
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
        self.updateRid()
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
        self.updateRid()
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
        print(url)
        if httpaction=="GET":
            encryptedresp=requests.get(url)
        elif httpaction=="POST":
            encryptedresp=requests.post(url,headers={"Content-Type": "application/aesjson-jd; charset=utf-8"},data=encrypteddata)
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

    # Do I really need this? I need to do getters and setters?¿
    # It isn't easier to simply use object.sessiontoken ?¿

    
    def getSessiontoken():
        """
        Returns the Sessiontoken, useful for apps so the user doesn't have to authenticate each time."
        """
        return self.sessiontoken
    def getRegaintoken():
        """
        Returns regaintoken, token used to reauthenticate if the sessiontoken has expired, useful for apps so the user doesn't have to authenticate each time .
        """
        return self.regaintoken
    def setSessiontoken(token):
        """
        Sets the sessiontoken
        """
        self.sessiontoken=token
    def setRegaintoken(token):
        """
        Sets the sessiontoken
        """
        
        self.regaintoken=token
