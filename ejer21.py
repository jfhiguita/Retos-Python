import requests
from bs4 import BeautifulSoup


def run(n):
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')

        with open(f'{name_file}.txt', 'w') as f:
            for title in soup.find_all(['h2','h3']):
                f.write(title.text + '\n')        


    
if __name__ == '__main__':
    name_file = input('What name do you want? ')
    run(name_file)
