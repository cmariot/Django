import sys


def parse_argument():
    """
    Parse the command line argument and return the filename
    Raises:
        ValueError: If the filename does not end with '.template'
    """

    if len(sys.argv) != 2:
        print("usage: python render.py 'filename.template'")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith(".template"):
        raise ValueError("Filename must end with '.template' extension")
    return filename


def read_template(filename):
    """
    Read the content of the file and return it
    Raises:
        FileNotFoundError: If the file is not found
    """

    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")


def read_settings():
    """
    Read the content of the settings.py file and return it as a dictionary
    Raises:
        FileNotFoundError: If the file is not found
        ValueError: If the settings format is invalid
    """
    try:
        settings = {}

        file_content = ""
        with open("settings.py", "r") as f:
            file_content = f.read()

        lines = file_content.splitlines()
        for line in lines:
            splitted_line = line.split(" = ")
            if len(splitted_line) != 2:
                raise ValueError(
                    "Invalid settings format, expected " +
                    "'key = value' format"
                )
            key, value = splitted_line
            banned_chars = ("<", ">")
            # Avoiding XSS attacks
            # first_name = "John<script>alert('XSS');</script>"
            for char in banned_chars:
                if char in value:
                    raise ValueError(
                        f"Disallowed character '{char}' in value"
                    )
            settings[key] = value.strip('"')
        return settings
    except FileNotFoundError:
        raise FileNotFoundError("File 'settings.py' not found")


def save_html(filename, rendered):
    html_filename = filename.replace(".template", ".html")
    with open(html_filename, "w") as f:
        f.write(rendered)


if __name__ == "__main__":
    try:
        filename = parse_argument()
        template = read_template(filename)
        settings = read_settings()
        rendered = template.format(**settings)
        save_html(filename, rendered)
    except Exception as e:
        print(e)
