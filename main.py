def addmultiplenumbers(num1, num2, num3):
    response = num1 + num2 + num3
    return response

def multiplymultiplenumbers(num1, num2, num3):
    response = num1 * num2 * num3
    return response

def isitaninteger(num):
    response = isinstance(num, int)
    return response

def isiteven(num):
    if isitaninteger(num):
        response = num % 2 == 0
    else:
        response = False
    return response

def addmultiplenumbers(num1, num2, num3):
    response = num1 + num2 + num3
    return response


def multiplymultiplenumbers(num1, num2, num3):
    response = num1 * num2 * num3
    return response


def isitaninteger(num):
    response = isinstance(num, int)
    return response


def isiteven(num):
    if isitaninteger(num):
        response = num % 2 == 0
    else:
        response = False
    return response


def main():
    print("Hello learners!")

    num1 = 2
    num2 = 3
    num3 = 4

    print("Suma:", addmultiplenumbers(num1, num2, num3))
    print("Multiplicación:", multiplymultiplenumbers(num1, num2, num3))
    print("¿Es entero?", isitaninteger(num3))
    print("¿Es par?", isiteven(num3))


if __name__ == "__main__":
    main()







