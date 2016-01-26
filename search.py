import argparse
import urllib.request
from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser(description="Search with your favorite browser and options")
    parser.add_argument("search", help="What you would like searched. *Quotes must be used*")
    args = parser.parse_args()
    search(args.search)


def search(search):
    try:
        response = urllib.request.urlopen("https://en.wikipedia.org/wiki/%s" % search)
        data = response.read()
        response.close()
        soup = BeautifulSoup(data,"html.parser")
        content = soup.find('div', id="bodyContent").p #gets first paragraph. would like to eventually get leading paragraphs above 'contents' box
        print(content.text)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()