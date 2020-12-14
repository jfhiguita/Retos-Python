import random
import string

def _pass_generator(n):
    
    letters = [random.choice(string.ascii_letters) for _ in range(int(n*0.5))]
    digits = [random.choice(string.digits) for _ in range(int(n*0.3))]
    special = [random.choice(string.punctuation) for _ in range(int(n*0.2))]

    contrasena = ''.join([letters,digits,special])
    #contrasena = letters + digits + special
    random.shuffle(contrasena)
    #contrasena = "".join(contrasena)
                          
    return contrasena


def run():

    n = int(input("How many elements: "))
    contrasena = _pass_generator(n)
    print(contrasena)

if __name__ == '__main__':
    run()
