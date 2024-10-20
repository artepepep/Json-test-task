import json
from typing import TypedDict

file_path = '/Users/mac/test-task-json/Json-test-task/data/data.json' # json file path
allowed_animals = {'dog', 'cat', 'cow', 'rat', 'alien'}

class Data(TypedDict): # annotate dict with json data
    field1: str
    animal: str


def read_json(json_path: str) -> Data:
    """
    Parses a JSON file and returns a dictionary with validated data.

    Args:
        json_path (str): The path to the JSON file.

    Returns:
        Data: Parsed and validated data.

    Raises:
        ValueError: If the 'animal' field contains an invalid value.
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        if data['animal'] not in allowed_animals:
            raise ValueError(f"Invalid animal: {data['animal']}. Must be one of: {', '.join(allowed_animals)}")
        return data


# bark, meow, moo, pipi, KILL
def animal_check(data: Data):
    """
    Check animal and make a sound depending on animal

    Args:
        data (dict): parsed json data

    Returns:
        None
    """
    match data['animal']:
        case 'dog':
            print('bark')
        case 'cat':
            print('meow')
        case 'cow':
            print('moo')
        case 'rat':
            print('pipi')
        case 'alien':
            print('KILL')

animal_check(read_json(file_path))