import unittest
import tempfile
import json
import os
from katas.json_config_merge import json_configs_merge  # replace with your actual import


class TestJsonConfigsMerge(unittest.TestCase):
    def write_temp_json(self, data):
        """Helper to create a temp JSON file and return its path."""
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix='.json')
        json.dump(data, temp_file)
        temp_file.close()
        return temp_file.name

    def test_merge_two_files(self):
        data1 = {
            "user": {"name": "John", "age": 30},
            "settings": {"theme": "light", "language": "english"}
        }
        data2 = {
            "user": {"age": 31, "email": "john@example.com"},
            "settings": {"language": "spanish", "timezone": "UTC+1"}
        }

        file1 = self.write_temp_json(data1)
        file2 = self.write_temp_json(data2)

        try:
            merged = json_configs_merge(file1, file2)
            expected = {
                "user": {"name": "John", "age": 31, "email": "john@example.com"},
                "settings": {"theme": "light", "language": "spanish", "timezone": "UTC+1"}
            }
            self.assertEqual(merged, expected)
        finally:
            os.remove(file1)
            os.remove(file2)

    def test_merge_multiple_files(self):
        data1 = {"a": 1, "b": {"x": 1}}
        data2 = {"b": {"y": 2}}
        data3 = {"a": 3, "b": {"x": 4}}

        file1 = self.write_temp_json(data1)
        file2 = self.write_temp_json(data2)
        file3 = self.write_temp_json(data3)

        try:
            merged = json_configs_merge(file1, file2, file3)
            expected = {
                "a": 3,
                "b": {"x": 4, "y": 2}
            }
            self.assertEqual(merged, expected)
        finally:
            os.remove(file1)
            os.remove(file2)
            os.remove(file3)



