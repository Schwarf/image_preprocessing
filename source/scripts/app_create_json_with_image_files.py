import json
import os
from typing import List
from source.data_access.files.implementations.json_file_reader import JSONFileReader

def get_list_of_files(dir_name: str) -> List[str]:
    list_of_directories = os.listdir(dir_name)
    file_list: List[str] = []
    for directory in list_of_directories:
        full_path = os.path.join(dir_name, directory)
        if os.path.isdir(full_path):
            file_list = file_list + get_list_of_files(full_path)
        else:
            file_name = os.path.basename(full_path)
            if file_name.endswith(".JPG"):
                file_list.append(full_path)

    return file_list


def create_json_label_file(file_list: List[str], image_path: str) -> None:
    #path = "D:/Data/image_data/labels/"
    path = "/media/linux_data/data/image_data/labels/"
    json_file_name = os.path.basename(image_path) + "_linux.json"
    default_label_value = -1
    default_label_dict = {os.path.normpath(file_name): default_label_value for file_name in file_list}
    file_handle = open(path + json_file_name, "w+")
    json.dump(default_label_dict, file_handle, indent=4)
    file_handle.close()


def replace_win_path_with_linux_path():
    label_file_path = ""
    windows_path = ""
    linux_path = ""
    reader = JSONFileReader()
    reader.open(label_file_path)
    data = reader.get_data()
    new_data = {}
    for key, value in data.items():
        new_key = key.replace(windows_path, linux_path)
        new_key = new_key.replace("\\", "/")
        new_data[new_key] = data[key]
    path = ""

    json_file_name = os.path.basename(path) + "my_camera_labeling_linux.json"
    file_handle = open(path + json_file_name, "w+")
    json.dump(new_data, file_handle, indent=4)


replace_win_path_with_linux_path()
#image_path = "D:/Data/image_data/images/my_camera"
#image_path = "/media/linux_data/data/image_data/labels/"
#file_list = get_list_of_files(image_path)

# create_json_label_file(file_list, image_path)
