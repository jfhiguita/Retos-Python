def _number(prompt):
    return int(input(prompt))

def run():

    number = _number("tell me a number: ")

    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    else:

        prime = True
        for i in range(2, int(number ** (1/2)+1)):
            if number % i == 0:
                prime = False
                break
            

    return prime
   
    

if __name__ == '__main__':
    prime = run()

    if prime:
        print("number is prime")
    else:
        print("number NOT is prime!")
