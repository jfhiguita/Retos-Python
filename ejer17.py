import requests
from bs4 import BeautifulSoup


def run():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')

        for title in soup.find_all(['h2','h3']):
            print(title.text)
        


    
if __name__ == '__main__':
    run()
