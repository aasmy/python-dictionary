import unittest
import os
import json
from driver import Dictionary
from file_handler import FileHandler, FileExtensions, InvalidFileTypeError


class TestDictionary(unittest.TestCase):

    def test_load_dictionary_json(self):
        """
        Tests loading a valid JSON file.
        """
        filename = "test_data.json"
        test_data = {"apple": "a fruit", "pear": "another fruit"}

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(test_data, file)

        my_dict = Dictionary()
        my_dict.load_dictionary(filename)

        self.assertTrue(my_dict._loaded)

        self.assertEqual(my_dict.query_definition("apple"), "a fruit")
        os.remove(filename)

    def test_query_case_insensitivity(self):
        """
        Tests that querying
        """
        filename = "test_case.json"
        test_data = {"Rain": "water from clouds"}
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(test_data, file)

        my_dict = Dictionary()
        my_dict.load_dictionary(filename)

        self.assertEqual(my_dict.query_definition("rain"), "water from clouds")
        self.assertEqual(my_dict.query_definition("RAIN"), "water from clouds")
        self.assertEqual(my_dict.query_definition("RaIn"), "water from clouds")

        os.remove(filename)

    def test_write_lines_to_txt(self):
        """
        Tests writing to a text file.
        """
        filename = "test_output.txt"
        lines_to_write = ["Hello World", "Testing 123"]

        FileHandler.write_lines(filename, lines_to_write)

        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        self.assertIn("Hello World", content)
        self.assertIn("Testing 123", content)

        os.remove(filename)

    def test_invalid_file_extension(self):
        """
        Tests that an exception is raised for unsupported files.
        """
        my_dict = Dictionary()

        try:
            my_dict.load_dictionary("image.png")

            self.fail("Did not raise InvalidFileTypeError")

        except InvalidFileTypeError:
            self.assertTrue(True)
        except Exception:
            self.fail("Raised wrong type of exception")


if __name__ == '__main__':
    unittest.main()