import pysrt  # Import the pysrt library
import os  # Import the os library


def change_charset(file_name):
    """
    This function converts the character encoding of a .srt file from ISO-8859-1 to UTF-8.
    :param file_name: the name of the .srt file to be converted
    """
    subs = pysrt.open(
        file_name, encoding='iso-8859-1')  # Open the .srt file with ISO-8859-1 encoding

    # Define a dictionary that maps special characters in ISO-8859-1 to their equivalent in UTF-8
    dictionar = {"º": "s", "ª": "S", "ş": "s", "Ş": "S",
                 "ţ": "t", "Ţ": "T", "þ": "t", "Þ": "T", "ã": "a", "Ã": "A",
                 "õ": "o", "Õ": "O", "ç": "c", "Ç": "C", "ñ": "n", "Ñ": "N",
                 "á": "a", "Á": "A", "é": "e", "É": "E", "í": "i", "Í": "I",
                 "ó": "o", "Ó": "O", "ú": "u", "Ú": "U", "ý": "y", "Ý": "Y",
                 "à": "a", "À": "A", "è": "e", "È": "E",
                 "Î": "I", "î": "i", "Â": "A", "â": "a"}

    # Loop over each subtitle in the file
    for sub in subs:
        # Replace each special character in the subtitle text with its equivalent in UTF-8
        for key, value in dictionar.items():
            sub.text = sub.text.replace(key, value)
    # Save the file back to disk with UTF-8 encoding
    subs.save(file_name, encoding="utf-8")
    # Print a message indicating that the file has been saved
    print(f"Done saving file {file_name}")


def main():
    """
    This function looks for all .srt files in the current directory and calls change_charset() on each of them.
    """
    # Loop over each item in the current directory
    for items in os.listdir():
        # Check if the item is a .srt file
        if items.endswith(".srt"):
            change_charset(items)


if __name__ == "__main__":
    # Call main() if the script is run as the main program (i.e., not imported as a module)
    main()
