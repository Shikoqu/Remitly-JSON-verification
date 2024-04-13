# Remitly-JSON-verification

This is a home exercise for the Remitly internship application. The project involves verifying JSON files.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Shikoqu/Remitly-JSON-verification.git
```

2. Navigate into the project directory:
```bash
cd Remitly-JSON-verification
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```
### Usage
Run the following command in the terminal to run the example program:
```bash
python main.py
```

#### Arguments
The program accepts the following arguments:
* `json_str`: The JSON string to be validated.
* `strict`: A boolean value that determines whether the JSON files should be validated against the schema. Defaults to `True`.

#### Wildcard Detection
The program will detect wildcards in the JSON files. The following is an example of a JSON file with a wildcard:
```json
{
  "PolicyName": "root",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": {
      "Sid": "IamListAccess",
      "Effect": "Allow",
      "Action": [
        "iam:ListRoles",
      ],
      "Resource": "*"
    }
  }
}
```

#### JSON Validation
If `strict` argument is `True`, the program will validate the JSON files against modified [aws-iam-poilcy-schema.json](https://gist.github.com/jstewmon/ee5d4b7ec0d8d60cbc303cb515272f8a?permalink_comment_id=4301718).

> Note: The original schema was modified to fit the requirements of the Remitly exercise.


### Running the tests
To run the tests, execute the following command in the terminal:
```bash
python -m unittest discover
```
or
```bash
python test_validator.py
```

## Project Structure
The project has the following structure:

* `json_schema.json`: The JSON schema against which the JSON files are validated.
* `json_validator.py`: The script that validates JSON files against the schema and checks for wildcards.
* `main.py`: The main script that runs the JSON validator.
* `test/`: This directory contains the test cases. Each subdirectory represents a different type of test case.
`test_validator.py`: The script that runs the tests.

---
## Authors
* **Jakub Wądrzyk** - [Shikoqu](https://github.com/Shikoqu)


## License
This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details.

