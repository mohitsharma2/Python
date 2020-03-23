"""
program to print whether a given character is an uppercase or 
a lowercase character or a digit or any other special character.

"""

inp1=input("Enter the Character:")
if inp1>='A' and inp1<="Z" :
    print("You entered upper case character.")
    
elif inp1>='a' and inp1<='z' :
    print("You entered lower case character.")
    
elif inp1>='0' and inp1<='9' :
        print("You entered numeric character.")

else:
        print("You entered special character.")
0

