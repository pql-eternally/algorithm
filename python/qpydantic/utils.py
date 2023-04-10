import json
import yaml


def json2yaml():
    with open('person/person.json') as f:
        data = json.load(f)
        print(data)

        with open('person/person.yaml', 'w') as yf:
            yaml.dump(data, yf, default_flow_style=False)
