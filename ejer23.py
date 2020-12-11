

def run():

    list1 = []
    
    with open('lista1_exe23.txt', 'r') as lista1:
        
        line = lista1.readline()

        while line:

            list1.append(int(line))
            line = lista1.readline()


    list2 = []

    with open('lista2_exe23.txt', 'r') as lista2:

        line = lista2.readline()

        while line:

            list2.append(int(line))
            line = lista2.readline()


    overlap = [item for item in list1 if item in list2]

    print(overlap)
            
        
    
 
    
if __name__ == '__main__':
    
    run()
