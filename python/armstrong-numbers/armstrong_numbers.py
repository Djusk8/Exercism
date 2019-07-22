def is_armstrong_number(number):

    arm_number = sum([int(num) ** len(str(number)) for num in str(number)])

    return True if arm_number == number else False
