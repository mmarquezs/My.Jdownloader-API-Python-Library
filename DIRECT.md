# Direct device access using My.JDownloader-API

This is an extension of myjdapi to allow a direct device access without My.JDownloader.

## Theory of operation

My.JDowloader manages JDownloader devices and myjdapi provides a python interface to access them.
If possible My.JDowloader will push a direct connection to myjdapi which will be used consequently.
If enabled this JDownloader api will be available locally. The direct access modification will make 
it possible to use the local api without any interaction with My.Downloader at all.

## Implemetation

In myjdapi all connetions will be managed by an instance of Myjdapi. To use myjdapi locally Myjdapi needs to be extended to allow local connextions.

`Myjdapi().connect_device(ip, port, _type='jd', username=None, password=None, timeout=None)` will create 
a local connection to a given device and it will make all modifications to the myjdapi instance to support 
the direct communication with the local device.

Even so the interface supports a user name and password it is not implemented yet.

The call to connect_device() will ping the device to make sure it exists and it will create a device with the name given by the ip-parameter and the id 'direct'.
A direct device connection has the status connected but it has no session id since the session id is supported be My.Downloader only.

## Usage

After myjdapi has established the connection the device can be querried as usually be calling:

```python
import myjdapi
host = 'localhost'
port = 3128
# We need an instance of Myjdapi() but no application key is required
jd = myjdapi.Myjdapi()
# connect directly to the device
jd.connect_device(host,port,timeout=10)
# The device can be accessed using the host name or ip address.
device = jd.get_device(host)
# Or the device can be accessed by using the device id "direct".
device = jd.get_device(device_id="direct")
```

Once the connection to the local device is established myjdapi will not connect to My.JDownloader any more. 
The connection is permanent and will not be refreshed any more.
