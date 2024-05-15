from sys import argv
import time
import re

tokensp = {
    "KEYWORD_KILL": r"KILL \*[0-9][0-9][0-9][0-9]",
    "KEYWORD_ENAP"
}