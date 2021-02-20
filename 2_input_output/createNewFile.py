filePath = "createNewFile.txt"
fileHandle = open(filePath, mode = 'x') # x for create new file
fileHandle.write(" Ini adalah file baru ")
fileHandle.close()

#open and read the file after create new file 
fileHandle = open(filePath, mode = 'r') # r for reading 
print(fileHandle.read())
fileHandle.close()