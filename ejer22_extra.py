

def run():
    
    category_dict = dict()
    
    with open('data_exer22_extra.txt', 'r') as f:
        
        line = f.readline()
        
        while line:
            
            line = line.strip()
            line = line.split('/')
            
            if line[2] in category_dict:
                category_dict[line[2]] += 1

            else:
                category_dict[line[2]] = 1

            line = f.readline()
            
    print(category_dict)
            
        
    
 
    
if __name__ == '__main__':
    
    run()
