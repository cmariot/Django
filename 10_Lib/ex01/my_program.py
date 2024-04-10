from local_lib.path import Path


def main():

    # Create a Directory
    p = Path("my_directory")

    if not p.exists():
        p.mkdir()

    # Create a File
    p = Path("my_directory/my_file.txt")
    p.write_text("The path module is correctly installed.")

    # Read the File
    p = Path("my_directory/my_file.txt")
    print(p.read_text())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
