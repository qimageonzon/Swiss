import os
from pathlib import Path

mapping_parent_path = Path("C:/Users/user/Desktop/Work Related/Labs SRF/Mapping Related")

for content in mapping_parent_path.iterdir():
    print(content)



import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            # print(json.dumps(data, indent=4))  # formatted output

            field_keys = [field['fieldKey'] for field in data.get('fields', [])]

            return field_keys




    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


for content in mapping_parent_path.rglob('*.json'):

    if content.name == "fields.json":

        content_list = read_json_file(content)

        print(sorted(content_list))
