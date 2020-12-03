import random

def run():

    n = int(input("How many numbers in the list?: "))
    lista = random.sample(range(100), n)

    new_list = [lista[0], lista[-1]]

    return print(lista, new_list, sep="\n")

    

if __name__ == '__main__':
    run()
