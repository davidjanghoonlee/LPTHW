# I am going to make a calculator
# These are the function protocols

# The addition
def add (x,y):
    return x+y

# The subtraction
def subtract (x,y):
    return x-y

# The multiplication
def multiply (x,y):
    return x*y

# The division
def divide (x,y):
    return x/y

# I am going to receive inputs from users


x = int(input("NUMBER INPUT 1: "))
y = int(input("NUMBER INPUT 2: "))


print "What do you want to do with the numberts? : "

print "1.ADD"
print "2.SUBTRACT"
print "3.MULTIPLY"
print "4.DIVIDE"



# Behavior based on the user's choice

choice = input(":")

if choice == '1':
    print x,"+",y,"=", add(x,y)

elif choice == '2':
    print x,"-",y,"=", subtract(x,y)

elif choice == '3':
    print x,"*",y,"=", multiply(x,y)

elif choice == '4':
    print x,"/",y,"=", divide(x,y)

else:
    print ("Invalid input")

#Why isn't this working?
# Mr.Olinda Please Help Me
# It seems like the functions are defined
