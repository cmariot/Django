import sys
import requests
import dewiki


def parse_arguments():
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <query>")
        return
    query = sys.argv[1]
    query = query.replace(" ", "_")
    return query


def main():

    query = parse_arguments()

    urls = (
        "https://en.wikipedia.org/w/api.php",
        "https://fr.wikipedia.org/w/api.php"
    )

    params = {
        "action": "query",          # fetch data
        "format": "json",           # format of the response
        "prop": "extracts",         # extract the content of the page
        "titles": query.lower(),    # title of the page
        "explaintext": True         # return plain text
    }

    extract = None

    for url in urls:

        response = requests.get(url, params=params)
        data = response.json()

        if not data or "query" not in data or "pages" not in data["query"]:
            continue

        pages = data["query"]["pages"]
        page_id = next(iter(pages))

        if page_id == "-1" or not pages[page_id]["extract"]:
            continue

        extract = pages[page_id]["extract"]

        if extract:
            break

    if extract:

        # Remove JSON or Wiki Markup formatting
        extract = dewiki.from_string(extract)

        # Create file name based on the query
        file_name = query + ".wiki"
        file_name = file_name.replace(" ", "_")

        # Write the result to a file
        with open(file_name, "w") as file:
            file.write(extract)

    else:
        print("No result found for the query.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
