#!/usr/bin/python
import sys

morse_code_lookup = {
    ".-":    "A",
    "-...":    "B",
    "-.-.":    "C",
    "-..":    "D",
    ".":    "E",
    "..-.":    "F",
    "--.":    "G",
    "....":    "H",
    "..":    "I",
    ".---":    "J",
    "-.-":    "K",
    ".-..":    "L",
    "--":    "M",
    "-.":    "N",
    "---":    "O",
    ".--.":    "P",
    "--.-":    "Q",
    ".-.":    "R",
    "...":    "S",
    "-":    "T",
    "..-":    "U",
    "...-":    "V",
    ".--":    "W",
    "-..-":    "X",
    "-.--":    "Y",
    "--..":    "Z",
    ".----":    "1",
    "..---":    "2",
    "...--":    "3",
    "....-":    "4",
    ".....":    "5",
    "-....":    "6",
    "--...":    "7",
    "---..":    "8",
    "----.":    "9",
    "-----":    "0"
}

def try_decode(bit_string):
    if bit_string in morse_code_lookup.keys():
        letter=morse_code_lookup[bit_string]
        #sys.stdout.write(letter)
        #sys.stdout.flush()
    return letter
