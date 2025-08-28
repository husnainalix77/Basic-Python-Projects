import string
fName = input('Enter your first name: ')
lName = input('Enter your last name: ')
pswd = input('Enter a password:') ## Husnain#2004

if ( len(pswd)<8 ):
    print('Length of password should be 8')
    
else:
    check1 = check2 = check3 = check4 = False
    for word in pswd:
        if (word  in string.ascii_uppercase) :
            check1 = True
        if (word in string.ascii_lowercase) :
            check2 = True
        if (word in string.punctuation) :
            check3 = True
        if (word in string.digits) :
            check4 = True

    if (check1 and check2 and check3 and check4) :
        if (fName.lower() in pswd.lower() or lName.lower() in pswd.lower()) :
            print('Try a different password')
        else:    
            print('Password Set Successfully')
    else:
        print('Not a valid password')  
                    
        