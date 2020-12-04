import random


def _is_in(lista, number, low, high):

    if low > high:
        return False

    middle = (low + high) // 2

    if number == lista[middle]:
        return True

    elif number < lista[middle]:
        return _is_in(lista, number, low, middle-1)

    else:
        return _is_in(lista, number, middle+1, high)

def run():

    number = -1
    lista = sorted(random.sample(range(0,30), 10))
    
    while (number < 0 or number > 30):
        number = int(input("Tell me a number between 0 and 30: "))

    is_in = _is_in(lista, number, low=0, high=len(lista)-1)
    

    print(lista, is_in, sep='\n')
    

if __name__ == '__main__':
    
    run()
