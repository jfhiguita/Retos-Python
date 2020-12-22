

def run():

    turn = ''
    while (turn != 'exit'):

        track = 0
        start = 0
        end = len(range(0,101))
        
        while True:
            
            track += 1
            machine_number = (start + (end - 1)) // 2
            print(machine_number)
            condition = input(f'Is your number {machine_number}: ').lower()

            if condition == 'too high':
                end = machine_number               
    
            elif condition == 'too low':
                start = machine_number + 1

            else:
                print("Exactly Right!!")
                print("Machine taken " + str(track) + " turns")
                print("E N D")
                break

        turn = input("si quieres salir type 'exit': ")
 
    

if __name__ == '__main__':
    run()
