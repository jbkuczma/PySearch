import argparse
import urllib.request
from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser(description="Quickly search Wikipedia")
    parser.add_argument("search", help="What you would like searched. *Quotes must be used*")
    args = parser.parse_args()
    search(args.search)


def search(search):
    try:
        search = search.replace(' ','_')
        response = urllib.request.urlopen("https://en.wikipedia.org/wiki/%s" % search)
        data = response.read()
        response.close()
        soup = BeautifulSoup(data,"html.parser")
        i = 0
        for i in range(len(soup.find_all('p'))):
            if(len(soup.findAll('p')[i].contents) == 0):
                break
            else:
                content = soup.findAll('p')[i]
                print(content.text)
                i+=1
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()