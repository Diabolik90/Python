def suma(a, b):
    return a + b;

def resta(a, b):
    return a - b

def multi(a,b):
    return a * b

def div(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    else:
        result = a / b
        return "{:6.2f}".format(result)