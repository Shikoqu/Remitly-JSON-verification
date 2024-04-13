import json
import jsonschema
from jsonschema import validate


def validate_json_schema(json_dict: dict, *, strict: bool = True) -> bool:
    """
    Validates a JSON dictionary against a JSON schema.
    
    :param json_dict: A JSON dictionary to validate.
    :param strict: Whether to validate against a strict JSON schema. Defaults to True.
    
    :return bool: Whether the JSON dictionary is valid according to the schema.
    
    :raises jsonschema.exceptions.ValidationError: If the JSON dictionary is valid but not according to the schema.
    """
    if strict:
        with open("json_schema_strict.json") as schema_file:
            schema = json.load(schema_file)
    else:
        with open("json_schema_notstrict.json") as schema_file:
            schema = json.load(schema_file)

    validate(instance=json_dict, schema=schema)
    return True


def validate_json(json_str: str, *, strict: bool = True) -> bool:
    """
    Returns logical false if an input JSON Resource field contains
    a single asterisk and true in any other case.
    
    Checks if a JSON string is valid against a JSON schema if strict is True.

    :param json_str: A JSON string to validate.
    :param strict: Whether to validate against a JSON schema. Defaults to True.

    :return bool: Whether the JSON string is valid. 

    :raises ValueError: If the JSON string is invalid.
    :raises jsonschema.exceptions.ValidationError: If the JSON string is valid but not according to the schema.
    """
    try:
        json_data: dict = json.loads(json_str)
        validate_json_schema(json_data, strict=strict)

        match json_data["PolicyDocument"]["Statement"]:
            case list() as statements:
                return all(s.get("Resource") != "*" for s in statements)
            case dict({"Resource": resource}):
                return resource != "*"
            case dict({"NotResource": resource}):
                return True
            case _:
                raise ValueError("Something went wrong")

    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON") from e
