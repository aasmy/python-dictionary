from enum import Enum
from pathlib import Path
import json

class FileExtensions(Enum):
    TXT = 'txt'
    JSON = 'json'

class InvalidFileTypeError(Exception):
    pass

class FileHandler:
    """
    class for handling file operations such as reading and writing.
    """
    @staticmethod
    def load_data(path, extension):
        """
        Reads data from a file based on the provided extension.

        :param path: The file path to read from.
        :param extension: The FileExtensions enum member (JSON or TXT).

        :return: A dictionary containing the loaded data.

        :raises FileNotFoundError: If the file path does not exist.
        :raises InvalidFileTypeError: If the extension is not supported.
        """
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} does not exist")

        if extension == FileExtensions.JSON:
            with open(file_path, 'r', encoding='utf-8') as file:
                raw_data = json.load(file)

                new_dictionary = {}
                for key, value in raw_data.items():
                    lowercase_key = key.lower()
                    new_dictionary[lowercase_key] = value

                return new_dictionary

        elif extension == FileExtensions.TXT:
            data = {}
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if ":" in line:
                        word, definition = line.strip().split(":", 1)
                        data[word.lower()] = definition
            return data

        else:
            raise InvalidFileTypeError(f"{file_path} is not a valid file type")

    @staticmethod
    def write_lines(path, lines):
        """
        Appends lines to a text file.

        :param path: The file path to write to.
        :param lines: A list of strings to write.
        """
        with open(path, 'a', encoding='utf-8') as file:
            for line in lines:
                file.write(line + "\n")