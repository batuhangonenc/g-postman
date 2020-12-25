"""
MIT License

Copyright (c) 2020 Batuhan Gonenc

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

"""

import os,sys
print("Postman Setup\n-------------")
un = os.getlogin()
try:
    file = open("/home/{}/.bashrc".format(un),'r')
    content = file.read()
    file.close()
except:
    print("something went wrong.")
    print("try execute again.")
    sys.exit()

here = os.getcwd()
new = '\nalias postman="cd {} && python3 postman.py"'.format(here)
newcontent = content + new

file = open("/home/{}/.bashrc".format(un),'w')
file.write(newcontent)
file.close()


try:
    os.system("sudo apt install python3-pygame")
    
except:
    os.system("pip3 install pygame")
    
print("Postman installed successfully.\njust write gpostman in terminal to use.")
li = input('press enter to exit')
os.remove("setup.py")
