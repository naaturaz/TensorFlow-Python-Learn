import subprocess
import os

clear = lambda: os.system('cls')
clear()

print("Save the world")

counter = 1000
miles = 1000.0
name = "John"

print( "counter +  miles: " + name)

# #subprocess.check_output(['ls','-l']) #all that is technically needed...
# print subprocess.check_output(['ls','-l'])

# dir = lambda: os.system('dir')
# dir()

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

def sum(a, b):
    res = a + b
    return res


printme("I'm first call to user defined function!")
printme("Again second call to the same function")

printme(sum(1, 2))



# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   mylist.append(["a",2,3,4])
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)






# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )




# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))




class ClassName:

    val1 = 1
    val2 = 2

    print("ClassName:")
    print(val1 + val2)

    sum = lambda self, arg1, arg2: arg1 + arg2

    def sum2(self, a, b):
        res = a + b
        return res
    

objC = ClassName()

sumObjC = objC.sum2(3, 3)
print(sumObjC)

sumObjD = objC.sum(4, 4)
print(sumObjD)


