

def run():
    
    n = int(input('tell me a number: '))
    lista = range(1, n+1)
    message = list(filter(lambda x: n % x == 0, lista))

    return print(message)


if __name__ == "__main__":
    run()
