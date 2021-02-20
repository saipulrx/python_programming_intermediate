# Python program to read 
# json file 
import json 

# Opening JSON string 
f = open('bitcoin.json','r') 

# load json string 
data = json.load(f) 

# Iterating through the json 
# list 
print(data)

# Closing file 
f.close() 