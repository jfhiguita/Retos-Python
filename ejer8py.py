def game(player1, player2):

    if player1 == player2:
        message = print("EMPATE!")
    elif player1 == "1":
        if player2 == "3":
            message = print("PLAYER1 WIN!")
        else:
            message = print("PLAYER2 WIN!!")
    elif player1 == "3":
        if player2 == "2":
            message = print("PLAYER1 WIN!")
        else:
            message = print("PLAYER2 WIN!!")
    elif player1 == "2":
        if player2 == "1":
            message = print("PLAYER1 WIN!")
        else:
            message = print("PLAYER2 WIN!!")

    return message
            


def eleccion(player):
    
    if player == "1":
        message = print("Your election is Rock")
    elif player == "2":
        message = print("Your election is Paper")
    elif player == "3":
        message = print("your election is Scissors")
    else:
        message = print("ERROR!, select a valid item")

    return message
    

def run():
        player1 = input("Cual eliges?: ")
        eleccion(player1)
        player2 = input("Cual eliges?: ")
        eleccion(player2)
        game(player1, player2)
        

        
 
    

if __name__ == '__main__':
    
    while True:
        print("""R O C K  -  P A P E R  -  S C I S S O R S

            Elige: 1. Rock
                   2. Paper
                   3. Scissors""")
        
        run()
        partida = input("Quieres jugar de nuevo?: ").lower()
        if partida == "no":
            break
        else:
            continue
 
