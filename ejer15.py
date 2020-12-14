

def _reverse(text):
    reverse = ''
    text = text.split()
    right = len(text)-1

    #reverse = lista[::-1]
    #result = ' '.join(reverse)

    while right >= 0:
        reverse += (text[right] + ' ')
        right -= 1
    
    return reverse


def run():

    n = input("Tell me multiple words: ")
    reverse = _reverse(n)
    print(reverse)

if __name__ == '__main__':
    run()
