import random

def _not_duplicates(lista):
    not_dupl = set(lista)

    return sorted(not_dupl)


def run():

    n = int(input("How many numbers: "))
    lista = [random.randint(0,50) for element in range(n)]
    not_dupl = _not_duplicates(lista)

    print (lista, not_dupl, sep="\n")
    

if __name__ == '__main__':
    run()
