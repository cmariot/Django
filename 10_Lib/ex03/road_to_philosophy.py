import sys
import requests
from bs4 import BeautifulSoup


def parse_argument():
    if len(sys.argv) != 2:
        raise Exception("usage: python3 road_to_philosophy.py query")
    query = sys.argv[1]
    if not query:
        raise Exception("Please provide a non-empty query")
    return query


def get_wiki_page(query):
    url = "https://en.wikipedia.org/wiki/" + query
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch the page: status code {response.status_code}"
        )
    return response.text


def get_page_title(soup, wiki_pages):
    title = soup.find("h1", {"class": "firstHeading"}).text
    if title in wiki_pages:
        print("It leads to an infinite loop !")
        exit(1)
    wiki_pages.append(title)
    return title


def print_result(wiki_pages, initial_query):
    print("\n".join(wiki_pages))
    print(f"{len(wiki_pages)} roads from {initial_query} to philosophy")
    exit(0)


def get_next_page(introduction_paragraph):
    query = None
    for paragraph in introduction_paragraph:
        links = paragraph.find_all("a")
        for link in links:
            href = link.get("href")
            if not href:
                continue
            splitted_link = href.split("/")
            if len(splitted_link) < 2:
                continue
            query = splitted_link[-1]
            if query is not None and "Help:" not in query:
                return query
    return None


if __name__ == "__main__":

    try:

        query = parse_argument()
        initial_query = query
        wiki_pages = []

        while (True):
            response = get_wiki_page(query)
            soup = BeautifulSoup(response, features="html.parser")
            title = get_page_title(soup, wiki_pages)
            if title == "Philosophy":
                print_result(wiki_pages, initial_query)
            wiki_content = soup.find(
                "div", {"class": "mw-content-ltr mw-parser-output"}
            )
            links_containers = ("p", "li")
            for container in links_containers:
                introduction = wiki_content.find_all(container)
                query = get_next_page(introduction)
                if query:
                    break
            if query is None:
                print("It leads to a dead end !")
                exit(1)

    except Exception as error:
        print(error)
