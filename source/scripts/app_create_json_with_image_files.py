import json
import os
from typing import List


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
    path = "D:/Data/image_data/labels/"
    json_file_name = os.path.basename(image_path) + ".json"
    default_label_value = -1
    default_label_dict = {os.path.normpath(file_name): default_label_value for file_name in file_list}
    file_handle = open(path + json_file_name, "w+")
    json.dump(default_label_dict, file_handle, indent=4)
    file_handle.close()


image_path = "D:/Data/image_data/images/my_camera"
file_list = get_list_of_files(image_path)

# create_json_label_file(file_list, image_path)
