import random

def run():
    n1 = int(input("Largo lista 1: "))
    n2 = int(input("Largo lista 2: "))
    
    lista1 = [random.randint(0, 50) for _ in range(n1)]
    lista2 = random.sample(range(50), n2)

    print(lista1, lista2, sep='\n')

    return print([element for element in set(lista1) if element in lista2])
    

if __name__ == '__main__':
    run()
