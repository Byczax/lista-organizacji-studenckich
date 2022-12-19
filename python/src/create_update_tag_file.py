import json_adapter as ja

SCRAP_DATA_PATH = "../../data/scrap_data.json"
TAG_DATA_PATH = "../../data/tags.json"
RESULTS_PATH = "../../data/results.json"


def create_tag_file():
    file_data = ja.read_file(SCRAP_DATA_PATH)
    tag_file = {}
    for data in file_data:
        tag_file[data["name"]] = []
    ja.save_to_file(TAG_DATA_PATH, tag_file)


def append_custom_tags():
    main_file = ja.read_file(SCRAP_DATA_PATH)
    tag_file = ja.read_file(TAG_DATA_PATH)

    for element in main_file:
        element["tags"] += tag_file[element["name"]]

    ja.save_to_file(RESULTS_PATH, main_file)


def main():
    if not ja.file_exists(SCRAP_DATA_PATH):
        print("There is no custom tags, creating template...")
        create_tag_file()
    append_custom_tags()


if __name__ == '__main__':
    main()
