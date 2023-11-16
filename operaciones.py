
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print(sumar(5, 3))

def restar(a, b):
    return a - b

if __name__ == "__main__":
    print(restar(5, 3))

def dividir(a, b):
   if b == 0:
        raise ValueError("No se puede dividir entre cero.")
   return a / b

if __name__ == "__main__":
    try:
        print( dividir(5, 0))
    except ValueError as e:
        print(f"Error: {e}")

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    print(multiplicar(5, 3)
