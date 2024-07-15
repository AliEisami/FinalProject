import json


class ConfigProvider:

    @staticmethod
    def load_from_file():
        """
            Loads configuration settings from a JSON file.
            Tries to open and read the configuration from '../config.json'.
            If the file is not found, it prints an error message and returns an empty dictionary.
            Returns:
                dict: Configuration settings loaded from the file or an empty dictionary if the file is not found.
        """
        try:
            with open('../config.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {file} not found. Starting with an empty library.")
