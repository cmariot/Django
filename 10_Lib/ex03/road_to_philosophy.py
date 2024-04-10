import sys
import requests
from bs4 import BeautifulSoup


def parse_argument():

    if len(sys.argv) == 1:
        return "Special:Random"
    if len(sys.argv) != 2:
        raise Exception("usage: python3 road_to_philosophy.py query")
    return sys.argv[1]


if __name__ == "__main__":

    try:

        query = parse_argument()

        wiki_pages = []
        while (True):

            url = "https://en.wikipedia.org/wiki/" + query

            response = requests.get(url)

            if response.status_code != 200:
                raise Exception("No result")

            soup = BeautifulSoup(response.text, features="html.parser")

            title = soup.find("h1", {"class": "firstHeading"}).text
            if title in wiki_pages:
                raise Exception(f"Infinite loop due to {title}")
            wiki_pages.append(title)
            print(title)

            if title == "Philosophy":
                exit(0)

            introduction_paragraph = soup.find(
                "div", {"class": "mw-content-ltr mw-parser-output"}
            ).find_all("p")

            query = None
            for paragraph in introduction_paragraph:

                links = paragraph.find_all("a")

                for link in links:

                    href = link.get("href")
                    if not href:
                        continue
                    splitted_link = href.split("/")
                    if len(splitted_link) != 3:
                        continue
                    query = splitted_link[-1]
                    if query is not None:
                        break

                if query is not None:
                    break

            if query is None:
                raise Exception("Mo link")

            # print(soup)
            # content = soup.find("div", {"id": "mw-content-text"})

            # paragraphs = content.find_all("p")
            # paragraphs.append(content.find("li"))

            # for paragraph in paragraphs:

            #     a = paragraph.find("a")
            #     if a:
            #         query = a.get("title")
            #         if query is not None:
            #             break
            #         continue
            # else:
                # raise Exception("No link found")

    except Exception as error:
        print(error)
