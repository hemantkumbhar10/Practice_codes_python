def is_valid(num1, num2, num3):
    if (num1 == num2+num3 or num1 > num2+num3):
        failure = ('These are not sides of triangle')
        return failure
    elif(num2 == num1 + num3 or num2 > num1 + num3):
        failure = ('These are not sides of triangle')
        return failure
    elif(num3 == num1+num2 or num3 > num1+num2):
        failure = ('These are not sides of triangle')
        return failure
    else:
        success = ('These are sides of traingle')
        return success

print(is_valid(3,3,2))