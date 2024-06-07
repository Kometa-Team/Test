import ruamel.yaml, os

path = "test.yml"

yaml = ruamel.yaml.YAML(typ='safe')
if not os.path.exists(path):
    with open(path, 'w'):
        pass

data = {"test": {"one": None, "two": "", "three": "null"}}

with open(path, 'w', encoding="utf-8") as fp:
    yaml.dump(data, fp)