import random

def _generate_number():
  pin = random.randint(0, 9999)
  
  return f'{pin:0{4}d}'


def run():
    track = 0
    user_num = ''
    generate_number = str(_generate_number())
    

    while (generate_number != user_num):
        cows = 0
        bulls = 0
        while (len(user_num) != 4):
          track += 1
          user_num = input('Give me a number (4 digits): ')

        #for i in range(len(generate_number)):
            #if user_num[i] == generate_number[i]:
          
        for idx, num in enumerate(generate_number):
          if user_num[idx] == num:
            cows += 1
          else:
            bulls += 1

        print(f'"Cows": {cows}', f'"Bulls": {bulls}', sep="\n")

        if cows != 4:
          user_num = ''
        else:
          break
        

    print(f'Your WIN, in {track} turns', f'the number is: {user_num}', sep='\n')

    
if __name__ == '__main__':
    print("""W E L C O M E  T O  T H E  C O W S  A N D  B U L L S  G A M E""")
            
    run()
