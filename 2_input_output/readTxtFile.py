filePath = "testIOPython.txt"
fileHandle = open(filePath, mode = 'r') # r for reading 
data = fileHandle.readline() # read into a variable 
print(data)
fileHandle.close()