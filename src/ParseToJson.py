from os import sync
from init import *


class C:
     def prompt():
        CTEMP = open("temp/c/Makefile", "r")
        Prompts.CPrompt()
        JSON_DATA = json.encoder(CTEMP)
        print(JSON_DATA)

C.prompt()