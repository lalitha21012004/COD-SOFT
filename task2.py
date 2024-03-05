print("Select an option from the following operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
option=int(input("enter a option:"))
result=0
if(option==1,2,3,4):

    if(option==1):
        num1=int(input("enter a number:"))
        num2=int(input("enter a number:"))
        result=num1+num2
    elif(option==2):
        num1=int(input("enter a number:"))
        num2=int(input("enter a number:"))
        result=num1-num2
    elif(option==3):
        num1=int(input("enter a number:"))
        num2=int(input("enter a number:"))
        result=num1*num2
    elif(option==4):
        num1=int(input("enter a number:"))
        num2=int(input("enter a number:"))
        result=num1//num2
else: 
   print("Invalid Input")       
   
print("the result of the given numbers is:{}".format(result))       



