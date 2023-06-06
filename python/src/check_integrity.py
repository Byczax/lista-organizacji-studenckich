import json_adapter

def main():
    jsons = json_adapter.read_file("../../data/parsed.json")
    mails = []
    json_mails = [json["email"].split(" ")[-1] for json in jsons]
    with open("../../data/mails.txt", "r") as file:
        mails = file.read().splitlines()
    print("\nMails in parsed.json:\n")
    for json in jsons:
        if "email" in json:
            if json["email"].split(" ")[-1] not in mails:
                print(json["email"].split(" ")[-1])   
    print("\nMails in mails.txt:\n")
    for mail in mails:
        if mail not in json_mails:
            print(mail)
                
    



if __name__ == '__main__':
    main()