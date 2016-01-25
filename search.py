import argparse
import webbrowser



def main():
    parser = argparse.ArgumentParser(description="Search with your favorite browser and options")
    parser.add_argument("search", help="What you would like searched. *Quotes must be used*")
    args = parser.parse_args()
    search(args.search)


def search(search):
    try:
        search = search.replace(' ', '+')
        webbrowser.open_new("https://www.google.com/#q="+search)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()