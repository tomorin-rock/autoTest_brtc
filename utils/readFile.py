import yaml
from autoTest_brtcApi.utils.getPath import get_yaml_path

def read_yaml(yaml_path):
    yml_path = get_yaml_path(yaml_path)
    with open(yml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    yaml_path = get_yaml_path("tmp.yml")
    data = read_yaml(yaml_path)
    print(data['data'])