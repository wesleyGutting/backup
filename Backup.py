import os
import hashlib
import shutil
import errno

BLOCK_SIZE = 65536
WORKING_PATH = 'C:\\Users\\wesle\\Desktop\\Colebrooke\\'
BACKUP_PATH = 'C:\\Users\\wesle\\Desktop\\Colebrooke 2\\'
TEST_PATH = 'C:\\Users\\wesle\\Desktop\\Software Dev\\Backup Program\\'

#-------------------------------------------------------------------------------

def calculateHash(input):
    md5_hash = hashlib.md5()
    with open(input, "rb") as f:
        content = f.read(BLOCK_SIZE)
        while len(content) > 0:
            md5_hash.update(content)
            content = f.read(BLOCK_SIZE)
    return md5_hash.hexdigest()
    f.close()

#-------------------------------------------------------------------------------

def generateDict(path):
    hashList = {}
    for dirPath, dirNames, fileNames in os.walk(path, topdown=True):
        dirNames[:] = [d for d in dirNames if not d.startswith('.')]
        print(f"Found Directory: {dirPath}")
        for file in fileNames:
            print(f"Generating hash for: {file}")
            hash = calculateHash(os.path.join(dirPath, file))
            print(f"--Hash: {hash}")
            hashList[hash] = os.path.join(dirPath, file)
    return hashList

#-------------------------------------------------------------------------------

def compareDicts(dict1, dict2):
    dict = {}
    update = dict1.keys() - dict2.keys()
    for key in update:
        dict[key] = dict1[key]
    return dict
#-------------------------------------------------------------------------------

backupDict = {}
workingDict = {}

print("Generating file hashes")
backupDict = generateDict(BACKUP_PATH)
workingDict = generateDict(TEST_PATH)

print("---------")

print("Backup Hashes:")
for key, value in backupDict.items():
    print(key, value)
print("Working Hashes:")
for key, value in workingDict.items():
    print(key, value)

print("---------")

updateDict = compareDicts(workingDict, backupDict)
for key, value in updateDict.items():
    print(f"Copying File: {value}")
