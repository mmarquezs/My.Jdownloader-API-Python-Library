# My.Jdownloader-API-Python-Library
## **DEVELOP BRANCH**

This a module for Python 2/3 to interact with My.Jdownloader. This is in a WIP project.You're free to use it following the MIT license and any collaboration is appreciated.

## How to use the api?
**NEW:** Now you can install it using pip from the pypi repo.
> pip install myjdapi

Example:

```python
#First of all you have to make an instance of the Myjdapi class and set your APPKey:
import myjdapi

jd=myjdapi.Myjdapi()
jd.set_app_key("EXAMPLE")

"""
After that you can connect.
Now you can only connect using username and password.
This is a problem because you can't remember the session between executions
for this reason i will add a way to "connect" which is actually not connecting, 
but adding the old tokens you saved. This way you can use this between executions
as long as your tokens are still valid without saving the username and password.
"""

jd.connect("email","password")

# When connecting it gets the devices also, so you can use them but if you want to 
# gather the devices available in my.jdownloader later you can do it like this

jd.update_devices()

# Now you are ready to do actions with devices. To use a device you get it like this:
device=jd.get_device("TEST") 
# The parameter by default is the device name, but you can also use the device_id.
device=jd.get_device(device_id="43434")

# After that you can use the different API functions.
# For example i want to get the packages of the downloads list, the API has a function under downloads called queryPackages,
# you can use it with this library like this:
device.downloads.query_packages([{
                "bytesLoaded" : True,
                "bytesTotal" : True,
                "comment" : False,
                "enabled" : True,
                "eta" : True,
                "priority" : False,
                "finished" : True,
                "running" : True,
                "speed" : True,
                "status" : True,
                "childCount" : True,
                "hosts" : True,
                "saveTo" : True,
                "maxResults" : -1,
                "startAt" : 0,
            }])
```


# LICENSE
The MIT License (MIT)

Copyright (c) 2015 Marc Marquez Santamaria

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
