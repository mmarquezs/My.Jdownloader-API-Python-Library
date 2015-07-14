class jdapi:
    api_url = "http://api.jdownloader.org"
    rid_counter = 0
    appkey = "MYJDAPI_php";
    apiVer = 1
    devices = []
    loginSecret = "";
    deviceSecret = "";
    sessiontoken = "";
    regaintoken = "";
    serverEncryptionToken = ""
    deviceEncryptionToken = ""
    SERVER_DOMAIN = "server"
    DEVICE_DOMAIN = "device";
    def __init__(self,email=None,password=None):
        self.data = []
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


