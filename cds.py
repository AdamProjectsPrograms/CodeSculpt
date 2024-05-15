from sys import argv
import time
import re

tokensp = {
    "KEYWORD_KILL": r"KILL \*[0-9][0-9][0-9][0-9]",
    "KEYWORD_ENAP_T": r"ENAP \@1",
    "KEYWORD_ENAP_F": r"ENAP \@0",
    "KEYWORD_MPTL": r"MPTL \*[0-9][0-9][0-9][0-9] : \\_[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]",
    "KEYWORK_"
}