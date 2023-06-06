import json_adapter

departments = {
    "W1": "W1 - Wydział Architektury",
    "W2": "W2 - Wydział Budownictwa Lądowego i Wodnego",
    "W3": "W3 - Wydział Chemiczny",
    "W4": "W4 - Wydział Informatyki i Telekomunikacji",
    "W5": "W5 - Wydział Elektryczny",
    "W6": "W6 - Wydział Geoinżynierii, Górnictwa i Geologii",
    "W7": "W7 - Wydział Inżynierii Środowiska",
    "W8": "W8 - Wydział Zarządzania",
    "W9": "W9 - Wydział Mechaniczno-Energetyczny",
    "W10": "W10 - Wydział Mechaniczny",
    "W11": "W11 - Wydział Podstawowych Problemów Techniki",
    "W12": "W12 - Wydział Elektroniki, Fotoniki i Mikrosystemów",
    "W13": "W13 - Wydział Matematyki"
}

organisations = [
    "Koło Naukowe",
    "Organizacja Studencka",
    "Agenda Kultury",
    "Media Studenckie"
]

def main():
    parsed_jsons = []
    jsons = json_adapter.read_file("../../data/results.json")
    for json in jsons:
        parsed_json = {}
        # check if the json has the key "email"
        if "email" in json:
            # print(json["email"])
            # check if the value of the key "email" is not empty
            # if "@pwr.edu.pl" in json["email"]:
            if "facebook" in json:
                parsed_json["facebook"] = json["facebook"].split(" ")[-1].replace("https://", "").replace("www.", "")
                
            if "website" in json:
                parsed_json["website"] = json["website"].split(" ")[-1].replace("https://", "").replace("www.", "")
                # if "www" not in parsed_json["website"]:
                    # parsed_json["website"] = "www." + parsed_json["website"]
                # print(parsed_json["website"])
                # print(parsed_json["facebook"])
            parsed_json["email"] = json["email"].split(" ")[-1]
            parsed_json["name"] = json["name"]
            parsed_json["description"] = json["description"]
            tags = json["tags"]
            for tag in tags:
                if tag in departments:
                    parsed_json["department"] = departments[tag]
                elif tag in organisations:
                    parsed_json["organisation"] = tag
                # else:
                    # print(f"Unknown tag: {tag}")
            parsed_jsons.append(parsed_json)
                # print the value of the key "email"
                # print(json["email"].split(" ")[-1])
        # print(json)
    print(len(parsed_jsons))
    json_adapter.save_to_file("../../data/parsed.json", parsed_jsons)


if __name__ == "__main__":
    main()
