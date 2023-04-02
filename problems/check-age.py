def checkAge(age):
    if age < 18:
        return 'You are minor'
    else:
        return 'You are an adult'

print(checkAge(19))