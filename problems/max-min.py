# Maximum
def checkmax():
    x= input('enter first number: ')
    y= input('enter second number: ')
    z= input('enter third number: ')
    if x > y:
        if x > z: return x 
        else : return z
    else :
        if y > z: return y
        else : return z

maxnumber=checkmax()
print('Maximum number is: ' + maxnumber)
