def checkAge(age):
    if age < 18:
        return 'You are minor'
    else:
        return 'Adult'

print(checkAge(17))