

def square(height, width):

    print(" ___" * width) 
    print("")
    print("|   " * (width+1))
    print("")

    if height == 1:
        print(" ---" * width)
    else:
        pass


    

def run():

    size = input("what size do you want? (3x2,4x4,etc...) ").split('x')
    height = int(size[0])

    if len(size) == 2:
        
        width = int(size[1])
    else:
        width = 1

    while height > 0:
        
        square(height, width)
        height -= 1



if __name__ == '__main__':
    
    run()
