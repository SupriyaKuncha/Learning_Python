print("hello World")
#Strings, integer
first_name = "Supriya"
age = 22
fav_food = "Dosa"
email = "youNoneed@fake.com"
#intro to format literals, same as template literals in JS
print(f"Mention f before the string. This is how you say it's f-string")
print(f"My name is {first_name}, I am {age} years old. I love {fav_food} and if you wanna talk more about {fav_food}, e-mail me at {email}")
#float, boolean
cgp= 9.19
is_student= False
if is_student==True :
    print(f"My Cgpa is {cgp}")
else :
    print("you are not a student")
#type casting using str(), int(), float(), bool()
integer = 22
integer = str(integer)
print(f"integer is type casted to {type(integer)}")
string = "s"
name=string
string = bool(string)
print(f"string is type casted to {type(string)}")
#if the string is empty, the bool will be false
#if the string have atleast one character, the bool will be true
#For example, This is useful to check if the person has entered the name
print(f"name given? {string}")

if string :
    print(f"Your name is {name}")
else :
    print("Enter your name")
float = 23.2
float = int(float)
print(f"float is type casted to {type(float)}")
boolean = True
#input : A function that prompts user to enter data and returns the entered data as string.
fav_music = input("What is your fav music? ")
print(f"{fav_music} is an excellent choice, you have great taste!")
my_age = input("Enter your age..")
print(f"age is of type {type(my_age)}")
# print (my_age+1) TypeError: can only concatenate str (not "int") to str
#input() take any value as string, even the number is considered as string. so if you want the numeric data to be considered as integer or float or any other data type, we need to type cast it.
my_age=int(my_age)
print("after type casting my_age from string to integer")
print(f"next year you will be {my_age+1}")
# directly typecasting the input , reduce lines and more readable.
my_height=int(input("Enter your height? "))
print (f"My height is {my_height} and is of type {type(my_height)}")
