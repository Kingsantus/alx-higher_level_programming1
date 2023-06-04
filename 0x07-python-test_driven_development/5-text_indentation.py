#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char_remove = [".", ":", "?"]
    line = ""
    word = ""

    for i in text:
        line += i
        if i in char_remove:
            word += line.strip() + "\n\n"
            line = ""

    if line:
        word += line.strip()

    print("{}".format(word), end="")
