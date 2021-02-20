filePath = "writeFile.txt"
fileHandle = open(filePath, mode = 'a') # r for append
fileHandle.write("\nAda tambahan isi txt file ")
fileHandle.close()

#open and read the file after the appending:
fileHandle = open(filePath, mode = 'r') # r for reading 
print(fileHandle.read())
fileHandle.close()