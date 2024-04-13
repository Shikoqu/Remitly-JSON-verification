from json_validator import validate_json

example_json = """
{
  "PolicyName": "root",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "IamListAccess",
        "Effect": "Allow",
        "Action": [
          "iam:ListRoles",
          "iam:ListUsers"
        ],
        "Resource": "*"
      }
    ]
  }
}
"""

example_json_2 = """
{
  "PolicyDocument": {
    "Statement":{
      "Resource": ":)"
    }
  }
}
"""

def main():
    print(validate_json(example_json))
    print(validate_json(example_json_2, strict=False))


if __name__ == "__main__":
    main()
