# -*- encoding: utf-8 -*-
import hashlib
import hmac
import json
import time
try:
    from urllib.request import urlopen
    from urllib.parse import quote
except:                         #For Python 2
    from urllib import quote
    from urllib import urlopen
import base64
import requests
from Crypto.Cipher import AES
BS = 16

def PAD(s):
    try:
        return s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    except:                     # For python 2
        return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def UNPAD(s):
    try:
        return s[0:-s[-1]]
    except:                     # For python 2
        return s[0:-ord(s[-1])]

class linkgrabber:
    """
    Class that represents the linkgrabber of a Device
    """
    def __init__(self, device):
        self.device = device
        self.url = '/linkgrabberv2'

    def set_enabled(self, params):
        """
        NOT WORKING

        My guess is that it Enables/Disables a download, but i haven't got it working.

        :param params: List with a boolean (enable/disable download), my guess
        the parameters are package uuid, download uuid. Ex:
        [False,2453556,2334455].
        :type: List
        :rtype:

        """
        resp = self.device.action(self.url+"/setEnabled", postparams=params)
        self.device.jd.updateRid()
        return resp

    def get_variants(self, params):
        """
        Gets the variants of a url/download (not package), for example a youtube
        link gives you a package with three downloads, the audio, the video and
        a picture, and each of those downloads have different variants (audio
        quality, video quality, and picture quality).

        :param params: List with the UUID of the download you want the variants. Ex: [232434]
        :type: List
        :rtype: Variants in a list with dictionaries like this one: [{'id':
        'M4A_256', 'name': '256kbit/s M4A-Audio'}, {'id': 'AAC_256', 'name':
        '256kbit/s AAC-Audio'},.......]
        """
        resp = self.device.action(self.url+"/getVariants", postparams=params)
        self.device.jd.updateRid()
        return resp

    def query_links(self, params=(
            {
                "bytesTotal"    : True,
                "comment"       : True,
                "status"        : True,
                "enabled"       : True,
                "maxResults"    : -1,
                "startAt"       : 0,
                "hosts"         : True,
                "url"           : True,
                "availability"  : True,
                "variantIcon"   : True,
                "variantName"   : True,
                "variantID"     : True,
                "variants"      : True,
                "priority"      : True
            })):
        """

        Get the links in the linkcollector/linkgrabber

        :param params: A dictionary with options. The default dictionary is
        configured so it returns you all the downloads with all details, but you
        can put your own with your options. All the options available are this
        ones:
        {
        "bytesTotal"    : false,
        "comment"       : false,
        "status"        : false,
        "enabled"       : false,
        "maxResults"    : -1,
        "startAt"       : 0,
        "packageUUIDs"  : null,
        "hosts"         : false,
        "url"           : false,
        "availability"  : false,
        "variantIcon"   : false,
        "variantName"   : false,
        "variantID"     : false,
        "variants"      : false,
        "priority"      : false
        }
        :type: Dictionary
        :rtype: List of dictionaries of this style:

[   {   'availability': 'ONLINE',
        'bytesTotal': 68548274,
        'enabled': True,
        'name': 'The Rick And Morty Theory - The Original        Morty_ - '
                'Cartoon Conspiracy (Ep. 74) @ChannelFred (192kbit).m4a',
        'packageUUID': 1450430888524,
        'url': 'youtubev2://DEMUX_M4A_192_720P_V4/d1NZf1w2BxQ/',
        'uuid': 1450430889576,
        'variant': {   'id': 'DEMUX_M4A_192_720P_V4',
                       'name': '192kbit/s M4A-Audio'},
        'variants': True},
    {   'availability': 'ONLINE',
        'bytesTotal': 68548274,
        'enabled': True,
        'name': 'The Rick And Morty Theory - The Original Morty_ - '
                'Cartoon        Conspiracy (Ep. 74) @ChannelFred (720p).mp4',
        'packageUUID': 1450430888524,
        'url': 'youtubev2://MP4_720/d1NZf1w2BxQ/',
        'uuid': 1450430889405,
        'variant': {'id': 'MP4_720', 'name': '720p MP4-Video'},
        'variants': True},
        .....]
        """
        resp = self.device.action(self.url+"/queryLinks", postparams=params)
        self.device.jd.updateRid()
        return resp

    def moveto_downloadlist(self, params):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        resp = self.device.action(self.url+"/moveToDownloadlist", postparams=params)
        self.device.jd.updateRid()
        return resp

    def add_links(self, params=[
            {
                "autostart" : False,
                "links" : "",
                "packageName" : "",
                "extractPassword" : "",
                "priority" : "DEFAULT",
                "downloadPassword" : "",
                "destinationFolder" : ""
            }]):
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
        resp = self.device.action("/linkgrabberv2/addLinks",postparams=params)
        self.device.jd.updateRid()
        return resp

    def add_container(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def get_childrenchanged(self):
        """
        no idea what parameters i have to pass and/or i don't know what it does.
        if i find out i will implement it :p
        """
        pass

    def set_priority(self):
        """
        no idea what parameters i have to pass and/or i don't know what it does.
        if i find out i will implement it :p
        """
        pass

    def remove_links(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def get_downfolderhistoryselectbase(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def help(self):
        """
        It returns the API help.
        """
        resp = self.device.action("/linkgrabberv2/help", "GET")
        self.device.jd.updateRid()
        return resp

    def rename_link(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def move_links(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def set_variant(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def get_package_count(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def rename_package(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def query_packages(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def move_packages(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

    def add_variant_copy(self):
        """
        No idea what parameters i have to pass and/or i don't know what it does.
        If i find out i will implement it :P
        """
        pass

class downloads:
    """
    Class that represents the downloads list of a Device
    """
    def __init__(self, device):
        self.device = device
        self.url = "/downloadsv2"

    def query_links(self, params=(
            {
                "bytesTotal" : False,
                "comment" : False,
                "status" : False,
                "enabled" : False,
                "maxResults" : -1,
                "startAt" : 0,
                "packageUUIDs" : False,
                "host" : False,
                "url" : False,
                "bytesloaded" : False,
                "speed" : False,
                "eta" : False,
                "finished" : False,
                "priority" : False,
                "running" : False,
                "skipped" : False,
                "extractionStatus" : False
            })):
        """
        Get the links in the download list
        """
        resp = self.device.action(self.url+"/queryLinks",postparams=params)
        self.device.myjd.updateRid()
        return resp

class jddevice:
    """
    Class that represents a JDownloader device and it's functions
    """
    def __init__(self, jd, device_dict):
        """ This functions initializates the device instance.
        It uses the provided dictionary to create the device.

        :param device_dict: Device dictionary
        """
        self.name = device_dict["name"]
        self.device_id = device_dict["id"]
        self.device_type = device_dict["type"]
        self.myjd = jd
        self.linkgrabber = linkgrabber(self)
        self.downloads = downloads(self)

    def action(self, action = False, params = False, postparams = False):
        """Execute any action in the device using the postparams and params.
        All the info of which params are required and what are they default value, type,etc
        can be found in the MY.Jdownloader API Specifications ( https://goo.gl/pkJ9d1 ).

        :param params: Params in the url, in a list of tuples. Example:
        /example?param1=ex&param2=ex2 [("param1","ex"),("param2","ex2")]
        :param postparams: List of Params that are send in the post.

        """
        if not action:
            return False
        httpaction = "POST"
        actionurl = self.__actionUrl()
        if not actionurl:
            return False
        if postparams:
            post = []
            for postparam in postparams:
                if isinstance(postparam, dict):
                    keys = list(postparam.keys())
                    data = "{"
                    for param in keys:
                        if isinstance(param, bool):
                            data += '\\"'+param+'\\" : '+str(postparam[param]).lower()+','
                        elif isinstance(param, str):
                            data += '\\"'+param+'\\" : \\"'+postparam[param]+'\\",'
                        else:
                            data += '\\"'+param+'\\" : '+str(postparam[param])+','
                    data = data[:-1]+"}"
                    post += [data]
                else:
                    data = []
                    if isinstance(postparam, bool):
                        data = [str(postparam).lower()]
                    elif isinstance(postparam, int):
                        data = ['\\"'+str(postparam)+'\\"']
                    elif isinstance(postparam, list):
                        data = ['\\"'+str(postparam)+'\\"']
                    else:
                        data = postparam
                    post += data
            if not params:
                text = self.myjd.call(actionurl, httpaction, rid=False, \
                postparams=post, action=action)
            else:
                text = self.myjd.call(actionurl, httpaction, rid=False, \
                params=params, postparams=post, action=action)
        else:
            text = self.myjd.call(actionurl, httpaction, rid=False, action=action)
        if not text:
            return False
        return text['data']

    def __action_url(self):
        if not self.myjd.sessiontoken:
            return False
        return "/t_"+self.myjd.sessiontoken+"_"+self.device_id


class myjdapi:
    """
    Main class for connecting to JD API.

    """
    def __init__(self, email=None, password=None, session_token=None, regain_token=None):
        """
        This functions initializates the myjdapi object.
        If email and password are given it will also try to connect
        with that account.
        If it fails to connect it won't provide any error,
        you can check if it worked by checking if session_token
        is not an empty string.
        TODO: Improve this ^^

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        """

        self.request_id = int(time.time()*1000)
        self.api_url = "http://api.jdownloader.org"
        self.app_key = "http://git.io/vmcsk"
        self.app_version = 1
        self.__devices = []
        self.login_secret = None
        self.device_secret = None
        self.session_token = session_token
        self.regain_token = regain_token
        self.server_encryption_token = None
        self.device_encryption_token = None
        self.email = email
        self.password = password

    def __secret_create(self, email, password, domain):
        """
        Calculates the login_secret and device_secret

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        :param domain: The domain , if is for Server (login_secret) or Device (device_secret)
        :return: secret hash

        """
        secret_hash = hashlib.sha256()
        secret_hash.update(email.lower().encode('utf-8') + password.encode('utf-8') + \
                    domain.lower().encode('utf-8'))
        return secret_hash.digest()

    def __update_encryption_tokens(self):
        """
        Updates the server_encryption_token and device_encryption_token

        """
        if self.server_encryption_token is None:
            old_token = self.login_secret
        else:
            old_token = self.server_encryption_token
        new_token = hashlib.sha256()
        new_token.update(old_token + bytearray.fromhex(self.session_token))
        self.server_encryption_token = new_token.digest()
        new_token = hashlib.sha256()
        new_token.update(self.device_secret+bytearray.fromhex(self.session_token))
        self.device_encryption_token = new_token.digest()

    def __signature_create(self,key,data):
        """
        Calculates the signature for the data given a key.

        :param key:
        :param data:
        """
        signature = hmac.new(key, data.encode('utf-8'), hashlib.sha256)
        return signature.hexdigest()

    def __decrypt(self,secret_token,data):
        """
        Decrypts the data from the server using the provided token

        :param secret_token:
        :param data:
        """
        init_vector = secret_token[:len(secret_token)//2]
        key = secret_token[len(secret_token)//2:]
        decryptor = AES.new(key, AES.MODE_CBC, init_vector)
        decrypted_data = UNPAD(decryptor.decrypt(base64.b64decode(data)))
        return decrypted_data

    def __encrypt(self,secret_token,data):
        """
        Encrypts the data from the server using the provided token

        :param secret_token:
        :param data:

        """
        data = PAD(data.encode('utf-8'))
        init_vector = secret_token[:len(secret_token)//2]
        key = secret_token[len(secret_token)//2:]
        encryptor = AES.new(key, AES.MODE_CBC, init_vector)
        encrypted_data = base64.b64encode(encryptor.encrypt(data))
        return encrypted_data.decode('utf-8')

    def update_request_id(self):
        """
        Updates Request_Id
        """
        self.request_id = int(time.time())

    def connect(self, email, password):
        """Establish connection to api

        :param email: My.Jdownloader User email
        :param password: My.Jdownloader User password
        :returns: boolean -- True if succesful, False if there was any error.

        """
        self.login_secret = self.__secret_create(email, password, "server")
        self.device_secret = self.__secret_create(email, password, "device")
        response = self.call("/my/connect", "GET", request_id=True, \
                             params=[("email", email), ("appkey", self.app_key)])
        if response is None:
            return False
        self.update_request_id()
        self.session_token = response["session_token"]
        self.regain_token = response["regain_token"]
        self.__update_encryption_tokens()
        self.update_devices()
        return True

    def reconnect(self):
        """
        Reestablish connection to API.

        :returns: boolean -- True if successful, False if there was any error.

        """
        if not self.session_token:
            return False
        response = self.call("/my/reconnect", "GET", request_id=True, \
                             params=[("session_token", self.session_token), \
                                     ("regain_token", self.regain_token)])
        if response is None:
            return False
        self.update_request_id()
        self.session_token = response["session_token"]
        self.regain_token = response["regain_token"]
        self.__update_encryption_tokens()
        return True

    def disconnect(self):
        """
        Disconnects from  API

        :returns: boolean -- True if successful, False if there was any error.

        """
        if not self.session_token:
            return False
        response = self.call("/my/disconnect", "GET", request_id=True, \
                             params=[("session_token", self.session_token)])
        if response is None:
            return False
        self.update_request_id()
        self.login_secret = None
        self.device_secret = None
        self.session_token = None
        self.regain_token = None
        self.server_encryption_token = None
        self.device_encryption_token = None
        return True

    def update_devices(self):
        """
        Updates available devices. Use list_devices() to get the devices list.

        :returns: boolean -- True if successful, False if there was any error.
        """
        if self.session_token is None:
            return False
        response = self.call("/my/listdevices", "GET", request_id=True, \
                             params=[("session_token", self.session_token)])
        if response is None:
            return False
        self.update_request_id()
        self.__devices = response["list"]
        return True

    def list_devices(self):
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

    def get_device(self, device_id=None, device_name=None):
        """
        Returns a jddevice instance of the device

        :param deviceid:
        """

        if device_id is not None:
            for device in self.__devices:
                if device["id"] == device_id:
                    return jddevice(self, device)
        elif device_name is not None:
            for device in self.__devices:
                if device["name"] == device_name:
                    return jddevice(self, device)
        return False

    def call(self,url,httpaction="GET",request_id=True,params=False,postparams=False,action=False):
        if not action:
            if (params):
                call=url
                for index,param in enumerate(params):
                    if index==0:
                        call+="?"+param[0]+"="+quote(param[1])
                    else:
                        call+="&"+param[0]+"="+quote(param[1])
                        # Todo : Add an exception if the param is login_secret so it doesn't get url encoded.
                if request_id:
                    call+="&request_id="+str(self.request_id)
                if not self.server_encryption_token:
                    call+="&signature="+str(self.__signaturecreate(self.login_secret,call))
                else:
                    call+="&signature="+str(self.__signaturecreate(self.server_encryption_token,call))
            if (postparams):
                pass
        else:
            call=url+action
            if (params):
                for index,param in enumerate(params):
                    if index==0:
                        call+="?"+param[0]+"="+quote(param[1])
                    else:
                        call+="&"+param[0]+"="+quote(param[1])
                        # Todo : Add an exception if the param is login_secret so it doesn't get url encoded.
                if request_id:
                    call+="&request_id="+str(self.request_id)
                if not self.server_encryption_token:
                    call+="&signature="+str(self.__signaturecreate(self.login_secret,call))
                else:
                    call+="&signature="+str(self.__signaturecreate(self.server_encryption_token,call))
            if (postparams):
                data='{"url":"'+action+'","params":["'
                for index,param in enumerate(postparams):
                    if index != len(postparams)-1:
                        data+=param+'","'
                    else:
                        data+=param+'"],'
            else:
                data='{"url":"'+action+'",'
            data+='"request_id":'+str(self.request_id)+',"apiVer":1}'
            print(data)
            encrypteddata=self.__encrypt(self.device_encryption_token,data);

        url=self.api_url+call
        print(url)
        if httpaction=="GET":
            encryptedresp=requests.get(url)
        elif httpaction=="POST":
            encryptedresp=requests.post(url,headers={"Content-Type": "application/aesjson-jd; charset=utf-8"},data=encrypteddata)
        if encryptedresp.status_code != 200:
            return False
        if not action:
            if not self.server_encryption_token:
                response=self.__decrypt(self.login_secret,encryptedresp.text) 
            else:
                response=self.__decrypt(self.server_encryption_token,encryptedresp.text)
        else:
            if (params or postparams):
                response=self.__decrypt(self.device_encryption_token,encryptedresp.text)
            else:
                response=encryptedresp.text
                return {"data" : response}
        jsondata=json.loads(response.decode('utf-8'))
        if jsondata['request_id']!=self.request_id:
            return False
        return jsondata

    # Do I really need this? I need to do getters and setters?¿
    # It isn't easier to simply use object.session_token ?¿

    
    def getSession_Token():
        """
        Returns the Session_Token, useful for apps so the user doesn't have to authenticate each time."
        """
        return self.session_token
    def getRegain_Token():
        """
        Returns regain_token, token used to reauthenticate if the session_token has expired, useful for apps so the user doesn't have to authenticate each time .
        """
        return self.regain_token
    def setSession_Token(token):
        """
        Sets the session_token
        """
        self.session_token=token
    def setRegain_Token(token):
        """
        Sets the session_token
        """
        
        self.regain_token=token
