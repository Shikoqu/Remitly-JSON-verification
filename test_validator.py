from io import TextIOWrapper
from typing import Generator
import os
import unittest
import jsonschema

from json_validator import validate_json


class TestJsonValidator(unittest.TestCase):
    @staticmethod
    def get_test_cases(directory: str) -> Generator[TextIOWrapper, None, None]:
        """
        Get test files in specified directory.

        :param directory: Dictionary with test cases jsons.
        
        :return Generator: Generator that yields requested test files.
        """

        files = os.listdir(f"test/{directory}")
        files = [f"test/{directory}/{f}" for f in files if f.endswith(".json")]

        for f in files:
            with open(f, "r") as f:
                yield f

    def test_validate_json_invalid_json(self) -> None:
        files = TestJsonValidator.get_test_cases("json_invalid_json")

        for test_file in files:
            with self.assertRaises(ValueError):
                validate_json(test_file.read())
                print(f"\n\tTest case failed for file: {test_file.name}")

    def test_validate_json_invalid_json_schema(self) -> None:
        files = TestJsonValidator.get_test_cases("json_invalid_json_schema")

        for test_file in files:
            with self.assertRaises(jsonschema.exceptions.ValidationError):
                validate_json(test_file.read())
                print(f"\n\tTest case failed for file: {test_file.name}")

    def test_validate_json_strict_disabled(self) -> None:
        files = TestJsonValidator.get_test_cases("json_strict_disabled")

        for test_file in files:
            with self.assertRaises(jsonschema.exceptions.ValidationError):
                validate_json(test_file.read(), strict=False)
                print(f"\n\tTest case failed for file: {test_file.name}")

    def test_validate_json_false(self) -> None:
        files = TestJsonValidator.get_test_cases("json_false")

        for test_file in files:
            self.assertFalse(
                validate_json(test_file.read()),
                f"\n\tTest case failed for file: {test_file.name}",
            )

    def test_validate_json_true(self) -> None:
        files = TestJsonValidator.get_test_cases("json_true")

        for test_file in files:
            self.assertTrue(
                validate_json(test_file.read()),
                f"\n\tTest case failed for file: {test_file.name}",
            )


if __name__ == '__main__':
    unittest.main()
