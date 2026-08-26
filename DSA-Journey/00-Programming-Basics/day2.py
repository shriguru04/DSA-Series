#Python Casting Code
# Create an integer
x=int(10)

# Convert to float
y=float(10)
# Convert to string
z=str(10)
# Print values
print(x,y,z)

#Strings
print("shri")
print('shri')

#Assign String to a Variable
s="shri"
print(s)

#Strings are Arrays
a="shri"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
a="john"
print(len(a))

#Check String (use in key word)
txt = "The best things in life are free!"
print("free" in txt)

#Check if NOT(use not in key word)
txt = "The best theings in life are free!"
print("expencive" not in txt)

#Slicing
a="john"
print(a[1:3])

#Slice From the Start
a="john"
print(a[:2])


#Slice From the end
a="john"
print(a[1:])

#slice with negative
a=" Hello world!"
print(a[-5:-2])

#Upper Case
a="Hello world!"
print(a.upper())

#lower Case
a="Hello world!"
print(a.lower())

#Replace String
a="Hello world!"
print(a.replace("H" ,"j"))

#Split String
a= "Hello, World!"
print(a.split(","))

#String Concatenation
a="hello "
b="world!"
x=a+b
print(x)

#F-Strings
age=int(21)
a= f"My age is {age}"
print(a)

#Escape Character
a="my name is \"shri\" and"
