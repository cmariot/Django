def get_elements_from_file():
    elements = {}
    with open("periodic_table.txt", "r") as f:
        file_lines = f.read().splitlines()

        for line in file_lines:

            # Parse the line,
            # Line example :
            # Hydrogen = pos:0, number:1, small: H, molar:1.00794, electron:1

            # Split the line by "="
            name, properties = line.split("=")

            # Split the properties by ","
            properties = properties.split(",")

            # Parse the properties
            element = {}
            for prop in properties:
                key, value = prop.split(":")
                element[key.strip()] = value.strip()

            elements[name.strip()] = element

    return elements


def create_html_file(elements):

    with open("periodic_table.html", "w") as f:

        css = """

        html {
            background-color: #d0dae8;
            font-family: Helvetica, sans-serif;
        }

        h1 {
            text-align: center;
            margin-block: 30px;
            color: #424242;
            text-decoration: underline;
            font-weight: bold;
        }

        td {
            border: 1px solid #424242;
            text-align: center;
            padding: 5px;
            width: 100px;
            height: 100px;
            color: #424242;
        }

        .no-border {
            border: none;
        }

        td:not(.no-border) {
            background-color: #9bb3df;
            border-radius: 2px;
        }

        td:not(.no-border):hover {
            transform: scale(1.5);
            box-shadow: 0 0 10px 0px #424242;
            position: relative;
            z-index: 1;
        }

        h4 {
            margin: 0;
        }

        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }

        li {
            font-size: 0.7em;
        }

        .wrapper {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            grid-template-rows: repeat(5, 1fr);
            width: 100%;
            height: 100%;
            overflow: auto;
        }

        .name {
            grid-column: 1 / 6;
            grid-row: 3;
            font-size: .7em;
        }

        .number {
            grid-column: 1/3;
            grid-row: 1;
            font-size: 0.8em;
        }

        .small {
            grid-column: 3;
            grid-row: 2;
            font-size: 0.9em;
        }

        .molar {
            grid-column: 1/6;
            grid-row: 4;
        }

        .electron {
            grid-column: 1/6;
            grid-row: 5/6;
            font-size: 0.5em;
        }

        """

        # On click, open the wikipedia page of the element in a new tab
        js = """
        document.addEventListener("DOMContentLoaded", function() {
            let tds = document.querySelectorAll("td:not(.no-border)");
            tds.forEach(td => {
                td.addEventListener("click", function() {
                    let elementName = td.querySelector(".name").textContent;
                    window.open(
                        `https://en.wikipedia.org/wiki/${elementName}`,
                        "_blank"
                    );
                });
            });
        });
        """

        f.write("<!DOCTYPE html>\n")
        f.write("<html lang='en'>\n")
        f.write("<head>\n")
        f.write("<title>Periodic Table</title>\n")
        f.write("<meta charset='UTF-8'>\n")
        f.write("<style>\n")
        f.write(f"{css}\n")
        f.write("</style>\n")
        f.write("<script>\n")
        f.write(f"{js}\n")
        f.write("</script>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<h1>Periodic table of the elements</h1>\n")
        f.write("<table>\n")
        f.write("<tbody>\n")
        row, column = 0, 0
        for element_name, element_properties in elements.items():
            if column == 0:
                f.write("<tr>\n")
            while column < int(element_properties['position']):
                f.write("<td class='no-border'></td>\n")
                column += 1
                if column == 18:
                    f.write("</tr>\n")
                    column = 0
                    row += 1
            f.write("<td>\n")
            f.write("<ul class='wrapper'>\n")
            f.write(f"<li class='name'>{element_name}</li>\n")
            f.write(f"<li class='number'>{element_properties['number']}</li>\n")
            f.write(
                "<li class='small'><h4> " +
                f"{element_properties['small']}" +
                "</h4></li>\n"
            )
            f.write(
                "<li class='molar'>" +
                f"{element_properties['molar']}" +
                "}</li>\n"
            )
            f.write(
                "<li class='electron'>" +
                f"{element_properties['electron']}" +
                "</li>\n"
            )
            f.write("</ul>\n")
            f.write("</td>\n")
            column += 1
            if column == 18:
                f.write("</tr>\n")
                column = 0
                row += 1
        f.write("</table>\n")
        f.write("</body>\n")
        f.write("</html>\n")


if __name__ == "__main__":

    try:

        # Parse the file
        elements = get_elements_from_file()

        # Create a html file
        create_html_file(elements)

    except Exception as e:
        print(f"An error occurred: {e}")
