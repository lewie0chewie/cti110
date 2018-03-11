# CTI-110
# P3HW1 - Age Classifier
# Luis Ventura
# 3/11/2018

def main():
    
    userAge = int (input ("Please enter your age: "))

    # If the person is 1 year old or less, he/she is an infant.
    if userAge <= 1:
        print ("You are an infant")
    
    # If the person is older than one year, but younger than 13 years old, he/she is a child.    
    elif userAge < 13:
        print ("You are a child")
    
    # If the person is at least 13 years old, but less than 20 years old, he/she is a teenager.
    elif userAge < 20:
        print ("You are a teenager")
    
    # If the person is at least 20 years old, he/she is an adult.
    elif userAge >= 20:
        print ("You are an adult")

main()
