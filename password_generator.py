import random
import string

def _pass_generator(n):

    upper_letters = [random.choice(string.ascii_uppercase) for _ in range(int(n*0.3))]
    lower_letters = [random.choice(string.ascii_lowercase) for _ in range(int(n*0.3))]
    digits = [random.choice(string.digits) for _ in range(int(n*0.2))]
    special = [random.choice(string.punctuation) for _ in range(int(n*0.2))]

    contrasena = upper_letters + lower_letters + digits + special
    random.shuffle(contrasena)
    contrasena = "".join(contrasena)
                          
    return contrasena


def run():
    n = 0
    while (n < 5):
        n = int(input("How many characters? (minimiun 5 characters): "))
        
    contrasena = _pass_generator(n)
    print(contrasena)

if __name__ == '__main__':
    run()
