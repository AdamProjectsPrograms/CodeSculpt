from sys import argv
import time
import re
import zipfile
tokensp = {
    "KEYWORD_KILL": r"KILL \*[0-9][0-9][0-9][0-9]",
    "KEYWORD_ENAP_T": r"ENAP \@1",
    "KEYWORD_ENAP_F": r"ENAP \@0",
    "KEYWORD_MPTL": r"MPTL \*[0-9][0-9][0-9][0-9] : \\_[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\...",
    "KEYWORK_CSPT": r"CSPT \*[0-9][0-9][0-9][0-9] : \\_[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\.TCF",
    "INT": r"INT [0-9][0-9]h",
    "EXT": r"EXT",
    "TJM": r"TJM",
    "SRV": r"SRV \$[0-9] : [0-9][0-9]",
    "RAR": r"RAR",
    "ZIP": r"ZIP"
}
TJM_C = 0
def lexer(code):
    PaT = 0
    PaTnum = 0
    for line in open(code, "r").readlines():
        for PAT in tokensp.values():
            pattern = re.compile(PAT)
            mat = re.match(pattern, line)
            if mat != None:
                PaT = 1
                break
            else:
                pass
            PaTnum += 1
            
        if PaT == 1:
            pp = list(tokensp.values())
            print(re.compile(pp[PaTnum]))
        else:
            print(f"Unknown line: {line}")
lexer(argv[1])