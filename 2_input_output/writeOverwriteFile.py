filePath = "writeFile.txt"
fileHandle = open(filePath, mode = 'w') # r for append
fileHandle.write(" Oops isi file tertimpa ")
fileHandle.close()

#open and read the file after the appending:
fileHandle = open(filePath, mode = 'r') # r for reading 
print(fileHandle.read())
fileHandle.close()