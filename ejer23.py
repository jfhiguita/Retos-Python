

def file_txt(filename):
    lista = []

    with open(filename) as f:

        line = f.readline()
        while line:
            lista.append(int(line))
            line = f.readline()

    return lista
            

def run():

    list1 = file_txt('lista1_exe23.txt')
    list2 = file_txt('lista2_exe23.txt')

    overlap = [item for item in list1 if item in list2]

    print(overlap)

#    list1 = []
    
#    with open('lista1_exe23.txt', 'r') as lista1:
        
#        line = lista1.readline()

#        while line:

#            list1.append(int(line))
#            line = lista1.readline()


#    list2 = []

#    with open('lista2_exe23.txt', 'r') as lista2:

#        line = lista2.readline()

#        while line:

#            list2.append(int(line))
#            line = lista2.readline()
            
        
    
 
    
if __name__ == '__main__':
    
    run()
