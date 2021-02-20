# Python code to demonstrate namedtuple() and 
# Access by name, index and getattr() 

# importing "collections" for namedtuple() 
import collections 

# Declaring namedtuple() 
Student = collections.namedtuple('Student',['name','age','DOB']) 

# Adding values 
S = Student('Nandini','19','2541997') 

# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 

# Access using name 
print ("The Student name using keyname is : ",end ="") 
print (S.name) 

# Access using getattr() 
print ("The Student DOB using getattr() is : ",end ="") 
print (getattr(S,'DOB')) 