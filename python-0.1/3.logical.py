#logical operators
# not (its print the opposite value)
a = 80
b = 60
print(not True) # (not) print the opposite value 
print(not (a > b)) 

#and operator( work if both value are true )

val1 = True
val2 = True
val3 = False
print("and operator:",val1 and val2 ) # output will be true
print("and operator:",val1 and val3) #output will be false

#or operators (owrks if either one value is true)

num1 = True
num2 = False
num3 = True
print("or operator:",num1 or num2)
print("or operator:",num1 or num3)
print("or operator:", num2 or num2)#if both values are false then the output will also false
