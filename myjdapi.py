import hashlib
import hmac
import urllib

class jdapi:

    def __init__(self,email=None,password=None):
        self.rid_counter=int(time.time())
        self.api_url = "http://api.jdownloader.org"
        self.appkey = "myjdapi-python"
        self.apiVer = 1
        self.devices = []
        self.loginSecret = ""
        self.deviceSecret = ""
        self.sessiontoken = ""
        self.regaintoken = ""
        self.serverEncryptionToken = ""
        self.deviceEncryptionToken = ""

        if email!=None & password!=None:
            self.connect(email,password)
    def __secretcreate(email,password,domain):
        # Calculate the loginSecret and deviceSecret
        # email,password, domain (server,device)
        h = hashlib.sha256()
        h.update(email.lower()+password+domain.lower())
        secret=h.hexdigest()
        return secret
        
    def connect(email,password):
        # Establish connection to api
        self.loginSecret=self.__secretcreate(email,password,"server")
        self.deviceSecret=self.__secretcreate(email,password,"device")
        signature=
        get="/my/connect?email="+urllib.quote(email)+"&appkey="+urllib.quote(self.appkey)+"&rid="+self.rid_counter+
        
        pass
    def reconnect(email,password):
        # Restablish connection to api
        pass
    def disconnect(email,password):
        # Restablish connection to api
        pass
    def devices():
        # Lists available devices.
        pass


