#!/usr/bin/python3
"""
text_indentation module
takes an args which is a strings of text
loop through the args if it encounter [.,:,?] and '\'
it create a newline for the args
"""
def text_indentation(text):
    """
    text_indentation() check if the arg provide is string if not raise TypeError
    it loop through and ensure that if the condition of [.,:,?] and '\'
    makes a new line until nothing remain
    """
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
