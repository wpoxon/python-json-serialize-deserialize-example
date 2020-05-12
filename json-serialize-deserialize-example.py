#!/usr/bin/python -tt

import json  # see https://docs.python.org/3/library/json.html

# to run this program:  python3 json-serialize-deserialize-example.py
# to see what it did:   cat sample_file.json

# some arbitrary python data structure we want to serialize to a json file
# and then read back (from a json file into a python data structure)
sample_data = {
    'record_type': 'test-runs',
    'action': 'INSERT',
    'Fields': {
        'test-set-id': 'controller_reboot',
        'test-id': 'reboot_staggered_reboot',
        'status': 'Failed',
        'ticket-id': '1029016',
        'ticket-classification': 'Jira',
        'build-id': 'myproduct-5.1.0.9.0.012',
        'team': 'Security',
        'how-run': 'Automated',
        'platform': 'myplatform',
        'comments': 'Test run comments.'
    }
}


def main():
    """Main program"""

    global sample_data
    serialize_filename = "./sample_file.json"

    print(f'serializing the following python data structure to {serialize_filename}')
    print(sample_data)
    print('\n')
    with open(serialize_filename, 'w') as save_file:
        json.dump(sample_data, save_file)
        save_file.close()

    print(f'successfully wrote/serialized python data structure to {serialize_filename}')
    print('\n')
    print(f'about to read/deserialize python data structure from {serialize_filename}')

    with open(serialize_filename, 'r') as load_file:
        deserialized_data = json.load(load_file)
        load_file.close()

    print(f'successfully read/deserialized python data structure from {serialize_filename}')
    print(deserialized_data)


if __name__ == "__main__":
    main()

exit(0)
