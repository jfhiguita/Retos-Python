

def run():
    number = int(input('Tell me a number: '))

    if number % 2 == 0:
        message = print(number ' is even')
    else:
        message = print(number ' is odd')

    return message


if __name__ == "__main__":
    run()
