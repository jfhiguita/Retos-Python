import requests
from bs4 import BeautifulSoup


def run():
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')

        with open("practice.txt", "w") as f:
            for p in soup.find_all('p')[6:-6]:
                f.write(p.text)
                               
        
    
     
if __name__ == '__main__':
    run()
