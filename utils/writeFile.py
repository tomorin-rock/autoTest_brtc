import yaml
from autoTest_brtcApi.utils.getPath import get_yaml_path


def write_file(data):
    yaml_file = get_yaml_path('tmp.yml')
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, allow_unicode=True)


if __name__ == '__main__':
    res = {
        "data": {
            "userId": "1",
            "token": "2134"
        }
    }
    write_file(res)
