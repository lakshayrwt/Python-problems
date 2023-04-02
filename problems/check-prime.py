def checkPrime(number):
    count = 2
    while(count < number):
        if number % count == 0:
            return 'Not a prime'
        else:
            count = count + 1
    return 'Prime'


print(checkPrime(7))

