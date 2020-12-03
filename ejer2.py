

def run():
    number = int(input('Tell me a number: '))

    if number % 4 == 0:
        message = print('Super number!')
    elif number % 2 == 0:
        message = print(str(number) + ' is even')
    else:
        message = print(str(number) + " is odd")

    return message


if __name__ == "__main__":
    run()
