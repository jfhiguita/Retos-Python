

def run():
    lista = [1,1,2,3,5,8,13,21,4,6,2,9,0]
    message = list(filter(lambda x: x < 5, lista))

    return print(message)


if __name__ == "__main__":
    run()
