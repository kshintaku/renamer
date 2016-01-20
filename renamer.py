# Here we go at our first major project
# That failed miserable in C++
# To batch rename our files based on set parameters
import os
import re
import time
import sys


def renamer(target):
    os.chdir(target)
    for filename in os.listdir('.'):
        print filename
        filepair = filename.split(".")
        if filepair[-1] in ["avi", "mkv", "mpeg", "mov", "mp4", "mpg", "wmv", "rmvb", "ogg", "ogm", "rm", "vob", "amv",
                            "divx"]:
            extname = filepair.pop()
            if len(filepair) > 1:
                stringfile = "_".join(filepair)
            else:
                stringfile = filepair[0]
            # print stringfile
            fixedstring = stringfixer(stringfile)
            completestring = fixedstring + "." + extname
            print completestring
            #			time.sleep(3)
            if filename != completestring:
                records = open('records.txt', 'a')
                records.write(filename + ' : ' + completestring + '\n')
                records.close()
            os.rename(filename, completestring)
        else:
            print "not the file you want"


def stringfixer(string):
    m = re.sub(r'\[([^]]+)\]', "", string)
    m = re.sub(r'\(([^\)]+)\)', "", string)
    if m:
        string = m
    string = string.replace('_', ' ')
    string = string.replace('  ', ' ')
    string = string.replace('  ', ' ')
    string = string.replace('_', ' ')
    string = string.strip()
    string = string.replace(' ', '_')
    string = string.title()
    h = re.split(r'(?<=\w)_(?=\d\d)', string)
    if len(h) > 1:
        string = '_-_'.join(h)
    return string


print "Enter Directory to go to work."
filepath = raw_input('> ')
renamer(filepath)