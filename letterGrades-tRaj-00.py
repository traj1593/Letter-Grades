'''
Program: Letter Grades
Filename: letterGrades-tRaj-00.py
Author: Tushar Raj
Description: Compute final course grades for students based on percentage scores using a function.
Revisions: No revisions made
'''
#There is no import statement
#There are no literal constraint
#There are no class defined

def letterGrade(score): #fuction to calculate grade
    '''
    This function accepts the input from the main function and converts the numeric data into grade
    Input : accepts parameter score which is a numeric value
    output: returns the grade on basis of which grade range the numerical score falls
    '''
    if(score < 55):
        return("F")
    elif(55<=score<60):
        return("C-")
    elif(60<=score<65):
        return("C")
    elif(65<=score<70):
        return("C+")
    elif(70<=score<75):
        return("B-")
    elif(75<=score<80):
        return("B")
    elif(80<=score<85):
        return("B+")
    elif(85<=score<90):
        return("A-")
    elif(90<=score<95):
        return("A")
    else:
        return("A+")


def inputdata(number): #checks the user input is correct
    '''
    This function accepts the input from the user and checks if the value contains any special character,alphabets. it even checks that the value is not negative and lies in asked range
    Input: user input from the console which is string type
    output: returns converted strings into float data type
    '''
    count = 1
    special = "!@#$%^&*()-+?_=,<>/"
    alphabet = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
    while(count):
        if(any( i in alphabet for i in number)): #checks if the value entered in number variable is having any character or not
            print("****Please Enter the valid numeric score****\n") #prints the error message
            progress = input("Please enter if you want to continue with computation of a letter grade for a numerical score(y/n): ") #ask users if he wants to continue with program
            if( progress == 'y' or progress == 'Y' ):#checks the response of the user if its y, he asks to enter the diameter again
                number = input("\nEnter the numerical score: ")
            if( progress == 'n' or progress == 'N' ):#exits the program if response in n
                exit()
            continue
        elif (any( i in special for i in number)): #picks up each character from the number variable and then checks in special variable if it is present, if present run this elif
            print("****Input cant have special character. Please Enter the valid numeric score from 0 to 100.****\n")
            progress = input("Please enter if you want to continue with computation of a letter grade for a numerical score(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nEnter the numerical score: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        elif(float(number) < 0): #checks if the entered user input is negative
            print("****Please Enter the valid numeric score from 0 to 100****\n")
            progress = input("Please enter if you want to continue with computation of a letter grade for a numerical score(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nEnter the numerical score: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        else:
            converted_number = float(number)
            if(0<=converted_number<=100):
                return converted_number
            else:
                print("****Please Enter the valid numeric score in range from 0 to 100****\n")
                progress = input("Please enter if you want to continue with computation of a letter grade for a numerical score(y/n): ")
                if( progress == 'y' or progress == 'Y' ):
                    number = input("\nEnter the numerical score: ")
                if( progress == 'n' or progress == 'N' ):
                    exit()
                continue
            
                 
### Step 1: Announce, prompt and get response
#Announce
print("****Letter Grades****");
print("Program to compute a letter grade for a numerical score\n")

#Main program starts in next line
#Prompt user to get response
number = input("Enter the numerical score:")

### Step 2: Call function inputdata to check input is valid or not and lettergrade to convert score into grade

#Call function inputdata and check the input value is valid input
score = inputdata(number)
#call the letterGrade function to calculate the grade on the basis of Numeric score
grade = letterGrade(score)

### Step 3: Print the result
print("The letter grade for {0} percent is {1}.".format(score,grade))
print("\n****Letter Grade program ended ****")
