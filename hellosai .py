# Task 1
a = 10
b = 6
print(a & b)

# Task 2
x = 12
y = 5
print(x | y)

# Task 3
num = 8
print(~num)

# Task 4
a = 15
b = 9
print(a ^ b)

# Task 5
num = 7
print(num << 2)

# Task 6
num = 20
print(num >> 2)

# Task 7
a = int(input("Enter the Number"))
b = int(input("Enter the Number"))
print(a & b)


# Task 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a ^ b)

# Task 9
s = "hi"
print(s * 5)

# Tadsk 10
s = "python"
print(s * 3)

# Task 11
a = "super"
b = "man"

print(a + b)

# Task 12
a = "hello"
b = " "
c = "world"

print(a + b + c)

# Tasak 13
name = input("Enter your name: ")
print(name * 5)

# Task 14
a = input("Enter first string: ")
b = input("Enter second string: ")

print(a + b)

# Task 15
name = input("Enter your name: ")
print(type(name))

# Task 16
age = int(input("Enter your age: "))
print(age)
print(type(age))

# Task 17

sum1 = int(input("Enter your Num"))
sum2 = int(input("Enter your Num"))
print("Total ",sum1 + sum2)

# Task 18
m1 = int(input("Enter first mark: "))
m2 = int(input("Enter second mark: "))

avg = (m1 + m2) / 2
print("Average =", avg)

# Task 19
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = 3*a*2 + b - 2
print( result)

# task 20
num = input("Enter a number: ")
print( type(num))

num = int(num)
print( type(num))

# Task 21
num = input("Enter a number: ")

print( num[-1])

# Task 22
num = int(input("Enter a number: "))

print("Unit digit =", num % 10)

# task 23
num = int(input("Enter a number: "))

print("Number without last digit =", num // 10)

# Task 24
Sdigit = 7696
print((Sdigit // 10 ) % 10)

# Task 36
Marks = int(input("Enter your Marks"))
age = int(input("Enter your Age"))
if Marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission canceled because of age")
else:
    print("Admission canceled because of marks")

# Task 37
Agee = int(input("Enter your Age"))
height = int(input("Enter your height"))
weight = int(input("Enter your Weight"))

if Agee >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejeected low Weight")
    else:
        print("Rejected low Height")        
else:
    print("Rejected below age")
# Task 38
days = int(input("Enter the number 1 - 7:"))
match days:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
# Task 39
color = int(input("Enter number between 1 - 3: "))
match color:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

# Task 40
Fruit = int(input("Enter number between 1 - 4: "))
match Fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")