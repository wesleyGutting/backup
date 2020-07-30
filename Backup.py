import os
import time
import hashlib

def log(logContent):
    print(logContent)
    logFile.write(logContent+"\n")

def pathCheck(path):
    if(os.path.exists(path)):
        print(path + ": exists")
        return True
    else:
        print(path + ': does not exist')
        return False

def calculateHash(input):
    log(f"--Calculating md5 for: {input}")

    BLOCK_SIZE = 65536
    md5_hash = hashlib.md5()
    with open(input, "rb") as f:
        content = f.read(BLOCK_SIZE)
        while len(content) > 0:
            md5_hash.update(content)
            content = f.read(BLOCK_SIZE)
    log(f"----md5 Hash for: {input}: {md5_hash.hexdigest()}")
    return md5_hash.hexdigest()
    f.close()

# path = 'C:\\Users\\wesle\\Desktop\\Colebrooke\\'
path = 'C:\\Users\\wesle\\Desktop\\Software Dev\\Backup Program\\'

logTime = time.strftime("%y-%m-%dT%H%M%S", time.gmtime())

if(pathCheck(f"{path}.logs")==True):
    os.chdir(f"{path}.logs")
else:
    print(f'Creating {path}.logs')
    os.mkdir(f"{path}.logs")
    os.chdir(f"{path}.logs")

print(f"Current Working Directory: {os.getcwd()}")
logFile = open(logTime+"_log.txt", "w+")
os.chdir(path)

fileList = {}
for dirPath, dirNames, fileNames in os.walk(path, topdown=True):
    dirNames[:] = [d for d in dirNames if not d.startswith('.')]
    log(f'Found Directory: {dirPath}')
    for file in fileNames:
        log(f'Found File: {file}')
        fileList[file] = calculateHash(file)

print(fileList)
logFile.close()
