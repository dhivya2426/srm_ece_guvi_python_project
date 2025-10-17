input=input("enter a value")
reversed_input=""
for i in input:
    reversed_input=i+ reversed_input
if(input==reversed_input):
        print("it is a palindrome")
else:
        print("it is not a palindrome")    