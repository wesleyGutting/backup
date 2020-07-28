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

if(pathCheck(path+".logs")==True):
    os.chdir(path+".logs")
else:
    print(f'Creating {path}.logs')
    os.mkdir(path+".logs")
    os.chdir(path+".logs")
print(f"Current Working Directory: {os.getcwd()}")
logFile = open(logTime+"_LOG.txt", "w+")
os.chdir(path)

for dirPath, dirNames, files in os.walk(path, topdown=True):
    dirNames[:] = [d for d in dirNames if not d.startswith('.')]
    print(f'Found Directory: {dirPath}')
    logFile.write(f'Found Directory: {dirPath}\n')
    for fileName in files:
        print(fileName)
        logFile.write(fileName+"\n")\

logFile.close()
