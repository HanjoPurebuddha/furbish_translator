# This is a sample Python script.

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

def translate_to_furbish(english_text_list):
    translation_dict = {"for":"this"}
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
    furbish_translation = translate_to_furbish(english)
    write_text_list("furbish.txt", furbish_translation)
