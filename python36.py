#Implement a python code to get username and password. Validate using regular experssions. Conditions: Username should not exceed 10 characters. It can't have symbols. Password should have one upper case, one lower case, one number , one symbol and length minimum of 6.

def main():
    login()
    
def login():
    username="chandan"
    password="Cy@007"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("Welcome - Access Granted")
    else:
        print("Access Denied")

main()

