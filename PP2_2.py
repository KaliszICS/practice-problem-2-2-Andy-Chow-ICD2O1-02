'''
    Lesson: If and Else
    Author: Mr. Kalisz
    Date Created: October 15, 2024
    Date Last Modified: October15, 2024
'''


def q1(): 
    num = input("Input an integer: ")
    num = int(num)
    if num == 5:
        print("The number is Five")
    else:
        print("The number is not Five")
  #Write Assignment code here


def q2(): 
    num2 = input("Input a number: ")
    num2 = float(num2)
    if num2 >= 1:
        print("Positive")
    else:
        print("Negative")
  #Write Assignment code here

def q3():
    num3 = input("Input an integer: ")
    num3 = int(num3)
    if not num3%2:
        print("Even")
    else:
        print("Odd")
    

def q4():
    str1 = input('Type "Hello": ')
    if str1 == "Hello":
        print("The word is Hello")
    else:
        print("The word is not Hello")



#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()
# q4()