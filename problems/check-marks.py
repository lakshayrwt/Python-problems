def checkmarks(marks):
    if marks > 90 and marks <= 100 :
        return 'A'
    elif marks > 70 and marks < 89 :
        return 'B'
    else :
        return 'C'

print (checkmarks(100))