#!/usr/bin/env python3

import sys
import re

def argMode():
    if (len(sys.argv) != 3):
        printHelp()
        return
    str = sys.argv[2]
    parse(str)
    return

def consoleMode():
    str = input()
    parse(str)
    return

def fileMode():
    if (len(sys.argv) != 3):
        printHelp()
        return
    filename = sys.argv[2]
    try:
        with open(filename) as f:
            str = f.read()
            parse(str)
    except:
        print("file not found")
    return

def parse(str):
    hexString = re.sub('[^A-Fa-f0-9]', '', str)
    stringParse(hexString)
    print("")
    arrayParse(hexString)
    return

def stringParse(str):
    a = nSplit(str, 2)
    parsed = '\\x'.join(a)
    print("\\x"+parsed)
    return

def arrayParse(str):
    a = nSplit(str, 2)
    parsed = ', 0x'.join(a)
    print("0x"+parsed)
    return

def nSplit(str, n):
    a=[]
    for i in range(0, len(str), n):
        a.append(str[i:i+n])
    return a 

def printHelp():
    print(f"{sys.argv[0]} [option]")
    print("[options]")
    print(f"-a: {sys.argv[0]} -a \"0d0f0900f0\"   // load from argument")
    print(f"-c: {sys.argv[0]} -c                // load from console")
    print(f"-f: {sys.argv[0]} -f dir/filename   // load from file")
    return

    
MODE = {"-a": argMode, "-c": consoleMode, "-f": fileMode}

try:
    MODE[sys.argv[1]]()
except:
   printHelp() 
