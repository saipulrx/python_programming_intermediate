import os

filePath = "createNewFile.txt"
if os.path.exists(filePath):
    os.remove(filePath)
    print("file " + filePath + " berhasil di hapus ")
else:
    print("file tidak ada")