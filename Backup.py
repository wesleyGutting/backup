import os
import time

def pathCheck(path):
    if(os.path.exists(path)):
        print(path + ": exists")
        return 1
    else:
        print(path + ': does not exist')
        return 0

path = 'C:\\Users\\wesle\\Desktop\\Software Dev\\Backup Program\\'
# path = 'C:\\Users\\wesle\\Desktop\\Colebrooke'


logTime = time.strftime("%y-%m-%dT%H%M%S", time.gmtime())

if(pathCheck(path+"logs")==True):
    os.chdir(path+"logs")
else:
    print(f'Creating {path}logs')
    os.mkdir(path+"logs")
    os.chdir(path+"logs")

print(f"Current Working Directory: {os.getcwd()}")

logFile = open(logTime+"_LOG.txt", "w+")
os.chdir(path)

logFile.close()

#for dirpath, dirnames, files in os.walk(directory):
#    print(f'Found Directory: {dirpath}')
#    for file_name in files:
#        print(file_name)
