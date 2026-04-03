import os
# 获取yml文件文件的位置
def get_yaml_path(filename):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    yml_dir = os.path.join(root_dir,"data",filename)
    return yml_dir

# 获取日志文件的位置
def get_log_path():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(root_dir,"logs")
    return log_dir

if __name__ == '__main__':
    yaml_path = get_yaml_path("common.yml")
    print(yaml_path)