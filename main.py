# This is a sample Python script.
import json
import datetime
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_text_file(filename):
    with open(filename, "r") as file:
        text = file.readlines()
    return text

def write_text_list(filename, text_list):
    with open(filename, "w") as file:
        for line_of_text in text_list:
            file.write(line_of_text + "\n")

def write_text_json(filename, json):
    with open(filename, "w") as file:
        file.write(json)

def translate_to_furbish(english_text_list):
    furb_dict_text = read_text_file("dictionary.txt")
    translation_dict = {}
    for line in furb_dict_text:
        print(line)
        split = line.split("\t")
        if "/" in split[0]:
            further_split = split[0].split("/")
            for j in range(len(further_split)):
                furb_dict_text.append(further_split[j] + " " + split[1])
    for line in furb_dict_text:
        if len(line) > 5:
            print(line)
            split = line.split()
            translation_dict[split[0].lower()] = split[1].lower()
    translated_text = []
    for line in english_text_list:
        list_of_words = line.split()
        for w in range(len(list_of_words)):
            try:
                list_of_words[w] = translation_dict[list_of_words[w]]
            except Exception:
                continue
        new_line = " ".join(list_of_words)
        translated_text.append(new_line)
    return translated_text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    english = read_text_file("english.txt")
    for i in range(len(english)):
        english[i] = english[i].lower()
    furbish_translation = translate_to_furbish(english)

    ids = list(range(len(furbish_translation)))
    counter = 0

    tweet_dict = {"tweet_date_pairs": None}
    tweet_date_pairs = []
    for i in range(len(furbish_translation)):
        tweet_date = []
        tweet_date.append(furbish_translation[i])
        tweet_date.append(str(ids[i]))
        tweet_date_pairs.append(tweet_date)
    tweet_dict["tweet_date_pairs"] = tweet_date_pairs
    formatted_json = json.dumps(
        tweet_dict,
        indent=4,
        sort_keys=True
    )
    write_text_json("furbish.json", formatted_json)