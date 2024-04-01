from path import Path


def main():
    # Create a Directory
    p = Path("../local_lib/my_directory")
    p.mkdir()

    # Create a File
    p = Path("../local_lib/my_directory/my_file.txt")
    p.touch()

    # Write to a File
    p.write_text("Installation is complete.")

    # Read from a File
    print(p.read_text())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
