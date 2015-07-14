import hashlib

class jdapi:
    api_url = "http://api.jdownloader.org"
    rid_counter = 0
    appkey = "myjdapi-python"
    apiVer = 1
    devices = []
    loginSecret = ""
    deviceSecret = ""
    sessiontoken = ""
    regaintoken = ""
    serverEncryptionToken = ""
    deviceEncryptionToken = ""

    def __init__(self,email=None,password=None):
        self.rid_counter=int(time.time())
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


