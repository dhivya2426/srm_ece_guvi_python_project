input=input("enter a value:")
if(input.isalpha()):
    print("this is an alphabet")
elif(input.isdigit()):
    print("this is the digit")
elif(not input.isalnum()):
    print("this is a special character")
else:
    print("invalid format")
