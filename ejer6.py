
def _palindrome(text):

    text = text.lower()
    text = text.replace(' ', '')
    left, right = 0, len(text)-1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True
    

#    reverse_text = text[::-1]
#    if text == reverse_text:
#        return True
#    else:
#        return False


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
