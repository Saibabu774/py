print("laptop","mouse","keyboard", sep="|")
print("Hello World Welcome python" ,end="\n")

#variables

name = "Ravi"
age = 22
city = "Chennai"
print(name,age,city,sep="-")

#multiple assignment
name,age,student= "Meena",20,True
print(name,age,student)

#indexing
word="Python"
print(word[0], word[2],word[5])

# ARITHMETIC OPERATORS
print(25+10) # 35, ADDITION OPERATOR
print(50-20) # 30,SUBTRACTION OPERATOR
print(8*5) # 40, MULTIPLICATION OPERATOR
print(100/10) #10.0, DIVISION OPERATOR
print(10%3) # 1, MODULUS OPERATOR, GIVES THE REMINDER AS OUTPUT
print(2**4) # 16, EXPONENTIAL OPERATOR
print(20//3) # 6, FLOOR DIVISION, ROUNDS DOWN THE RESULT

# BODMAS EXPRESSION
print(3+2*5**2) 
''' ans is 53 
    using BODMAS rule, first exponential is calculated, 
    then multiplication and finally addition is calculated
'''

# ASSIGNMENT OPERATOR
num=50
num+=25
print(num)

num=100
num/=10
print(num)

#COMPARISON OPERATOR
print(10>5) # True
print(20<15) # False
print(5==5) # True
print(10!=8) # True
print(7>=7) # True
print(6<=2) # False

#STRING COMPARISON
a="apple"
b="Apple"

print(a==b) # False

print("a:", ord("a"))
print("A:", ord("A"))
''' As the ASCII value for a is 97 and A is 65, the result will be false'''

# TASK 10 - LOGICAL OPERATORS
print(10>5 and 5==5) # True
print(5>10 or 10==10) # True
print(not(5>2)) # False

# MEMBERSHIP OPERATOR

numbers=[10,20,30,40,50]
print(20 in numbers) # True
print(60 in numbers) # False
print(30 not in numbers) # False

#SWAP VARIABLES
a=10
b=20
a,b=b,a
print("a=",a)
print("b=",b)

# BITWISE XOR
a=6
b=3
print(a^b) # output is 5

