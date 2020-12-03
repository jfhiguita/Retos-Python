

def _reverse(text):
    lista = text.split()
    reverse = lista[::-1]
    result = ' '.join(reverse)
    
    return result


def run():

    n = input("Tell me multiple words: ")
    reverse = _reverse(n)
    print(reverse)

if __name__ == '__main__':
    run()
