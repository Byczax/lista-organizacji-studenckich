import requests
from bs4 import BeautifulSoup
# from colorama import Fore, Style
import json_adapter as ja


main_link = "https://dzialstudencki.pwr.edu.pl"
main_org = "/organizacje-studenckie/wykaz-uczelnianych-organizacji-studenckich"
button_id = "button-link"
org_id = "accordion text-content"
possible_domains = ["pwr.edu.pl", "pwr.wroc.pl", "www.pwr", "wroclaw.pl"]

departments = {
    "wydzial-architektury": "W1",
    "wydzial-budownictwa-ladowego-i-wodnego": "W2",
    "wydzial-chemiczny": "W3",
    "wydzial-informatyki-i-telekomunikacji": "W4",
    "wydzial-elektryczny": "W5",
    "wydzial-geoinzynierii--gornictwa-i-geologii": "W6",
    "wydzial-inzynierii-srodowiska": "W7",
    "wydzial-zarzadzania": "W8",
    "wydzial-mechaniczno-energetyczny": "W9",
    "wydzial-mechaniczny": "W10",
    "wydzial-podstawowych-problemow-techniki": "W11",
    "wydzial-elektroniki--fotoniki-i-mikrosystemow": "W12",
    "wydzial-matematyki": "W13"
}
types = {
    "kola-naukowe": "Koło Naukowe",
    "organizacje-studenckie": "Organizacja Studencka",
    "agendy-kultury": "Agenda Kultury",
    "media-studenckie": "Media Studenckie"
}


def dig_website(link):
    print(f'{link}')
    website = requests.get(link)
    soup = BeautifulSoup(website.content, 'html.parser')
    link_data = soup.find_all('a', class_=button_id)
    if len(link_data) == 0:
        return extract_data(soup, link)
    else:
        result = []
        for link in link_data:
            result += dig_website(main_link + link["href"])
        return result


def extract_data(soup, path):
    organisations = soup.find_all('div', class_=org_id)
    all_orgs = []
    for org in organisations:
        # print(Fore.MAGENTA + str(org) + Style.RESET_ALL)
        org_data = org.find_all('p')
        org_object = {}

        # organisation_object[""] = org.find
        org_object["description"] = ""

        org_object["name"] = org.find('button').text.strip()
        org_object["full_path"] = path
        for data in org_data:
            inside = data.text.strip()
            if len(inside) > 0:
                if "www.facebook.com" in inside:
                    org_object["facebook"] = inside
                elif "@" in inside:
                    org_object["email"] = inside
                elif any(link in inside for link in possible_domains):
                    org_object["website"] = inside
                else:
                    org_object["description"] += inside
        org_object["tags"] = get_tags(org_object)
        # full_object = {}
        # full_object[org_object["name"]] = org_object
        all_orgs.append(org_object)
    return all_orgs


def get_tags(object):
    tags = []
    department = object["full_path"].split("/")[-1]
    if department in departments:
        tags.append(departments[department])
        tags.append(types[object["full_path"].split("/")[-2]])
        tags.append(department.replace("-", " ").title())
    else:
        tags.append(types[department])
    return tags


def main():
    data = dig_website(main_link + main_org)
    print(len(data))
    ja.save_to_file("../../data/scrap_data.json", data)


if __name__ == '__main__':
    main()
