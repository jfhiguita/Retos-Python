import re

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

    formato = True

    while formato:

        size = input("what size do you want? (3x2,4x4,etc...) ")
        if re.search('^[0-9][x][0-9]', size):
            formato = False
            
    size = size.split('x')
    height = int(size[0])
    width = int(size[1])

    while height > 0:
        
        square(height, width)
        height -= 1



if __name__ == '__main__':
    
    run()
