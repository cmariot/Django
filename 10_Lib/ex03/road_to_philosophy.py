import sys
import requests
from bs4 import BeautifulSoup


def parse_argument():

    if len(sys.argv) != 2:
        raise Exception("usage: python3 road_to_philosophy.py query")
    return sys.argv[1]


if __name__ == "__main__":

    try:

        query = parse_argument()

        wiki_pages = []

        while (True):

            if query in wiki_pages:
                raise Exception("It leads to an infinite loop")

            wiki_pages.append(query)

            url = "https://en.wikipedia.org/wiki/" + query

            response = requests.get(url)

            if response.status_code != 200:
                raise Exception("No result")

            print(f"{len(wiki_pages)}: {query}")

            if query == "Philosophy":
                break

            soup = BeautifulSoup(response.text, features="html.parser")

            content = soup.find("div", {"id": "mw-content-text"})

            paragraphs = content.find_all("p")
            paragraphs.append(content.find("li"))

            for paragraph in paragraphs:

                a = paragraph.find("a")
                if a:
                    query = a.get("title")
                    if query is not None:
                        break
                    continue
            else:
                raise Exception("No link found")

    except Exception as error:
        print(error)
