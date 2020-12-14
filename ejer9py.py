import random

def run():

    turn = ''
    while (turn != 'exit'):

        track = 0       
        number = random.randint(1,9)
        
        while True:

            guess_number = 0
            
            while (guess_number not in range(1,10)):
                track += 1
                guess_number = int(input("what is the number? (SOLO numeros entre 1 y 9): "))

            if guess_number > number:
                print("Too Hight!!!")
            elif guess_number < number:
                print("Too low!")
            else:
                print("Exactly Right!!")
                print("Your taken " + str(track) + " turns")
                print("E N D")
                break

        turn = input("si quieres salir type 'exit': ")
 
    

if __name__ == '__main__':
    run()
