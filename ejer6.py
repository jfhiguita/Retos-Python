
def _palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    reverse_text = text[::-1]
    if text == reverse_text:
        return True
    else:
        return False


def run():
    text = input('Tell me a string: ')
    palindrome = _palindrome(text)
    if palindrome:
        message = print('YES...it\'s a palindrome!!!')
    else:
        message = print('NOOOOOooo...it\'s not a palindrome!!!')

    return message



    

if __name__ == '__main__':
    run()
