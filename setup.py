import os,sys
print("Postman Setup\n-------------")
un = input('enter your username in session:')

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

print("Postman installed successfully.\njust write postman in terminal to use.")
li = input('press enter to exit')
os.remove(setup.py)
