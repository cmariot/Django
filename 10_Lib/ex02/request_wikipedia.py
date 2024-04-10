import sys
import requests
import dewiki


def parse_arguments():
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <query>")
        return
    return sys.argv[1]


def search_wikipedia(url: str, query: str) -> list:

    # Opensearch : search for a query
    # Returns a list of search results

    params = {
        "action": "opensearch",
        "search": query,
        "format": "json",
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return

    data: dict = response.json()

    if not data:
        return
    elif len(data) < 2:
        return

    return data[1]


def request_wiki(url: str, query: str) -> str:

    params = {
        "action": "query",          # fetch data
        "prop": "extracts",         # Returns plain-text extracts of the page.
        "titles": query,            # title of the page
        "redirects": "true",        # follow redirects
        "format": "json",           # format of the response
        "explaintext": True         # return plain text
    }

    # Send a request to the Wikipedia API
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    # Parse the JSON response
    data: dict = response.json()
    if not data:
        return
    elif 'query' not in data:
        return
    elif 'pages' not in data['query']:
        return

    # Get the first page id from the response
    page_id = next(iter(data['query']['pages']))
    if page_id == "-1":
        print("Page not found")
        return

    # Remove Wiki Markup formatting from the extract of the page
    extract = dewiki.from_string(
        data['query']['pages'][page_id]['extract']
    )

    return extract


def save_extract(query: str, extract: str):

    # Create file name based on the query
    filename = (query + ".wiki").replace(" ", "_")

    # Write the result to a file
    with open(filename, "w") as file:
        file.write(extract)


def main():

    query = parse_arguments()

    urls = (
        "https://fr.wikipedia.org/w/api.php",
        "https://en.wikipedia.org/w/api.php"
    )

    extract = None

    for url in urls:

        list_of_results = search_wikipedia(url, query)

        for search_result in list_of_results:

            extract = request_wiki(url, search_result)
            if extract:
                save_extract(query, extract)
                exit()

    if not extract:
        print(f"Could not find the page for {query}")
        return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
