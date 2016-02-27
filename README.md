# My.Jdownloader-API-Python-Library

**INFO: I'm working on a new version on the 'develop' branch. It will change functions names and other things. So if you want to use this library  you might want to check that branch first, especially if you want to use python 2.7 since that branch supports it.**
**Also the API specifications provided by JDownloader Team have been improved and probably a lot of the functions I will be available to do them now with more information.**
**Finally, I will try to put it on PyPI so you can easily install it using 'pip'.**

This a module for Python 3 to interact with My.Jdownloader. This is in a WIP project.You're free to use it following the MIT license and any collaboration is appreciated.

To use this API you need to use a "APPkey".This APPkey can be anything you want but it's recommended to be something that identifies your project or a URL to it. Right now this module uses "http://git.io/vmcsk" as the APPKey, but this APPKey is intended just for testing and for little projects, it's recommended that you uses your own "APPKey" so if for some reason this APPKey gets blocked you don't get affected.


Right now the only things working are:
  - JD: 
    - Connect,Disconnect,Reconnect,GetDevices,listDevices
  - JD.Device:
    - action,addLinks

Example of usage:
```
import myjdapi

jd=myjdapi.myjdapi()
jd.connect("example@example.com","password")
jd.getDevices()
jd.getDevice(name="DeviceName").linkgrabber.addLinks([{"autostart" : False, "links" : "https://mega.nz/#!xxxxxxxxxxxxxxxxxxxxxxxxxxxx,http://mediafire.com/download/xxxxxxxxxxxxxxxx/","packageName" : "TEST" }])

```




# DOCUMENTATION

http://myjdownloader-api-python-library.readthedocs.org/en/latest/myjdapi.html#module-myjdapi

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
