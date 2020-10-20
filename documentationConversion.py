# -*- coding: utf-8 -*-
"""
Doxygen documentation conversion

Takes a .h file in input with documentation before each function, and prints
the documentation formatted for the beginning of the file. This is not perfect,
and you should remember to write the documentation for anything that is not
a function or a method by hand. You should also verify the \fn line, because
it only prints the whole line. You should add the class:: before the name,
and remove the words that are not needed.

I could improve this script, but it would take me more time that what it would
make me win.

Sorry I did not document the whole script, doing documentation for the main
program of my TM, feeling bored of documentation rn.

Created on Mon Oct 19 15:25:27 2020
@author: Joachim Favre
"""

FILE_PATH = "D:\\PathTracer\\PathTracer\\Ray.h"


def remove_all_characters_groups(string, character_group):
    list_without_groups = string.split(character_group)
    result = ""
    for part in list_without_groups:
        result += part
    return result


def format_line(line):
    formatted_line = remove_all_characters_groups(line, "\t")
    formatted_line = remove_all_characters_groups(formatted_line, "\n")
    return formatted_line


def line_begins_with(line, beginning):
    if len(line) < len(beginning):
        return False
    return line[0:len(beginning)] == beginning


def line_wo_beg(line, beginning):
    return line[len(beginning):len(line)]


total_doc = "\\file " + FILE_PATH.split("\\")[-1] + "\n\\brief \n\n"

with open(FILE_PATH) as file:
    current_doc = ""
    for line in file:
        formatted_line = format_line(line)
        if formatted_line != "":
            if line_begins_with(formatted_line, "//!"):
                current_doc += "\\brief" + line_wo_beg(formatted_line, "//!") + "\n"
                line = format_line(file.readline())
                if line_begins_with(line, "/*!") or line_begins_with(line, " /*!"):
                    line = format_line(file.readline())
                    while not line_begins_with(line, "*/") and not line_begins_with(line, " */"):
                        if line != "":
                            if line[0] != "\\":
                                current_doc += "\\details " + line + "\n"
                            else:
                                current_doc += line + "\n"
                        line = format_line(file.readline())
                    line = format_line(file.readline())
                current_doc = "\\fn " + line[0:-1] + "\n" + current_doc
                total_doc += current_doc + "\n"
                current_doc = ""
print(total_doc)
