import json
from typing import Any

def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Recursively merge d2 into d1.
    """
    for key, value in d2.items():
        if key in d1 and isinstance(d1[key], dict) and isinstance(value, dict):
            d1[key] = merge_dicts(d1[key], value)
        else:
            d1[key] = value
    return d1
def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    """
    Merge multiple JSON configuration files into a single dictionary.

    You are given an unknown number of file paths pointing to JSON configuration files.
    These files should be merged in the order they are given:
    - Keys in later files override those in earlier ones.
    - Nested dictionaries must also be merged recursively.

    Example:

        File: default.json
        {
          "user": {
            "name": "John",
            "age": 30
          },
          "settings": {
            "theme": "light",
            "language": "english"
          }
        }

        File: local.json
        {
          "user": {
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

        Result:
        {
          "user": {
            "name": "John",
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "theme": "light",
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

    Args:
        *json_paths: Variable number of JSON file paths to merge.

    Returns:
        dict: The merged configuration dictionary.
    """
    merged_config: dict[str, Any] = {}

    for path in json_paths:
        with open(path, 'r', encoding='utf-8') as f:
            current_config = json.load(f)
            merged_config = merge_dicts(merged_config, current_config)

    return merged_config


#if __name__ == '__main__':
    # Example usage; make sure the files exist for this to run.
    #config = json_configs_merge('default.json', 'production.json', 'us-east-1-production.json')
    #print(config)
