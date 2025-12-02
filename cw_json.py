import pickle
import string
import os

numbers = [1, 2, 3, 4, 5]

serialized_data = pickle.dumps(numbers)

print(f"serialized_data:\n {serialized_data}")

deserialized_data = pickle.loads(serialized_data)
print(f"deserialized_data: {deserialized_data}")


def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, file_name)


def serialize(file_name, data):
    with open(create_path(file_name), 'wb') as file:
        pickle.dump(data, file)


def deserialize(file_name):
    with open(create_path(file_name), 'rb') as file:
        data = pickle.load(file)
    return data


try:
    letters = [symbol for symbol in string.ascii_letters]
    file_name = "letters.data"

    print(f"Original data:\n {letters}\n")
    serialize(file_name, letters)
    letters_restored = deserialize(file_name)

    print(f"deserialized_data:\n {letters_restored}")

except Exception as ex:
    print(ex)

import json

capitals = {
    "Italy": "Rome",
    "Spain": "Madrid",
    "Germany": "Berlin"
}

s_capitals = json.dumps(capitals)
print(f" old capitals: {capitals}")
print(f"serial capitals: {s_capitals}")

print(json.loads(s_capitals))


def json_serialize(file_name, data):
    with open(create_path(file_name), 'w') as file:
        json.dump(data, file, indent=4)


def json_deserialize(file_name):
    with open(create_path(file_name), 'r') as file:
        data = json.load(file)
    return data


try:
    file_name = "employee.data"

    employees_dict = {
        "company": "Apple",
        "employees": [
            {
                "name": "Tim Cook",
                "age": 55,
                "skills": ["programing", 'communication', 'crm']
            },
            {
                "name": "Tim Cook 2",
                "age": 45,
                "skills": ["programing", 'communication', 'crm']
            }
        ]
    }

    json_serialize(file_name, employees_dict)
    des_dict = json_deserialize(file_name)
    print(f"before saving: {employees_dict}")
    print(f"After saving: {des_dict}")
except Exception as ex:
    print(ex)
