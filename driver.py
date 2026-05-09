from file_handler import FileExtensions, InvalidFileTypeError, FileHandler

class Dictionary:
    """
    Represents a dictionary that can load definitions and query words.
    """
    def __init__(self):
        self._data = dict()
        self._loaded = False

    def load_dictionary(self, filepath):
        """
        Determines the file type and loads the dictionary data.

        :param filepath: The path to the dictionary file (json or txt).
        """
        if filepath.endswith('.json'):
            ext = FileExtensions.JSON
        elif filepath.endswith('.txt'):
            ext = FileExtensions.TXT
        else:
            raise InvalidFileTypeError(f"File {filepath} is not supported.")

        self._data = FileHandler.load_data(filepath, ext)
        self._loaded = True

    def query_definition(self, word):
        """
        Retrieves the definition of a word from the loaded dictionary.

        :param word: The word to look up.

        :return: The definition(s) of the word, or None if not found.
        :raises Exception: If the dictionary has not been loaded yet.
        """
        if not self._loaded:
            raise Exception("Dictionary is not loaded")
        return self._data.get(word.lower())


def main():
    dictionary = Dictionary()
    try:
        dictionary.load_dictionary('data.json')
        print("Dictionary loaded successfully.")
    except (FileNotFoundError, InvalidFileTypeError) as e:
        print(f"Error loading dictionary: {e}")
        return

    while True:
        word = input('Enter a word (or "exitprogram" to quit): ')

        if word.strip() == 'exitprogram':
            break
        try:
            definition = dictionary.query_definition(word)

            if definition:
                if isinstance(definition, list):
                    formatted_def = "\n".join(definition)
                else:
                    formatted_def = str(definition)

                print(f"Definition: {formatted_def}")

                FileHandler.write_lines(
                    "data.txt",
                    [f"{word}: {formatted_def}"]
                )
            else:
                print("Word not found")

        except Exception as e:
            print(f"An error occurred during query: {e}")

if __name__ == '__main__':
    main()