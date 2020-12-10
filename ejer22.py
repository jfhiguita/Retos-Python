

def run():
    
    names_dict = dict()
    
    with open('data_exer22.txt', 'r') as f:
        
        line = f.readline()
        
        while line:
            
            line = line.strip()
            
            if line in names_dict:
                names_dict[line] += 1

            else:
                names_dict[line] = 1

            line = f.readline()
            
    print(names_dict)
            
        
    
 
    
if __name__ == '__main__':
    
    run()
