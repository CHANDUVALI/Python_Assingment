#Implement a program to check the elements of a list is a palindrome or not.

def isPalindrome(s): 
      
    # to reverse string print(s) 
    rev = ''.join(reversed(s)) 
  
    # Checking if both string are  
    # equal or not 
    if (s == rev): 
        return True
    return False
  
# main function 
s = input("enter the element to check:")
#s = "123431"
ans = isPalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No") 
